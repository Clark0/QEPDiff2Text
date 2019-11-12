from qepdiff2text.constants import NodeAttrs, Algos, Operations, OP_ALGS
from qepdiff2text.parser import parse_cond


def isOperation(algo, operation):
    return algo in OP_ALGS[operation]


def findOperation(algo):
    for operation in Operations.all():
        if isOperation(algo, operation):
            return operation
    return None


class Node(object):
    cur_table_name = 1
    cur_step = 1
    table_subquery_name_pair = {}
    steps = []

    def __init__(self, attrs, is_root=True):
        assert isinstance(attrs, dict)
        # assert NodeAttrs.NODE_TYPE in attrs
        self.algorithm = attrs[NodeAttrs.NODE_TYPE]
        self.operation = findOperation(self.algorithm)
        self.attributes = {k: v for k,
                           v in attrs.items() if k in NodeAttrs.all()}
        self.text = None
        self.step = None

        if self.is_scan():
            if self.algorithm == Algos.INDEX_SCAN:
                if attrs[NodeAttrs.RELATION_NAME]:
                    self.set_output_name(
                        attrs[NodeAttrs.RELATION_NAME] +
                        " with index " +
                        attrs[NodeAttrs.INDEX_NAME]
                    )
            elif self.algorithm == Algos.SUBQUERY_SCAN:
                self.set_output_name(attrs[NodeAttrs.ALIAS])
            else:
                self.set_output_name(attrs[NodeAttrs.RELATION_NAME])

        if NodeAttrs.PLANS in attrs:
            self.children = [Node(child_attrs, is_root=False)
                             for child_attrs in attrs[NodeAttrs.PLANS]]
            self.attributes.pop(NodeAttrs.PLANS)
        else:
            self.children = []
        if is_root:
            Node.init_node()
            self.to_text()

    @staticmethod
    def init_node():
        Node.cur_table_name = 1
        Node.cur_step = 1
        Node.table_subquery_name_pair = {}
        Node.steps = []

    def set_output_name(self, output_name):
        if "T" == output_name[0] and output_name[1:].isdigit():
            self.output_name = int(output_name[1:])
        else:
            self.output_name = output_name

    def get_output_name(self):
        if str(self.output_name).isdigit():
            return "T" + str(self.output_name)
        else:
            return self.output_name

    def is_scan(self):
        return self.operation == Operations.SCAN

    def __str__(self, show_algo=False):
        first_line = "- {}".format(self.algorithm if show_algo else self.operation)
        children_lines = [
            "\t" + line
            for child in self.children
            for line in child.__str__(show_algo).split("\n")
        ]
        return "\n".join([first_line] + children_lines)

    def to_text(self, skip=False) -> str:
        if self.text is not None:
            return self.text

        increment = True
        # skip the child if merge it with current node
        if self.algorithm in [Algos.UNIQUE, Algos.AGG] and len(self.children) == 1 \
                and (Operations.SCAN in self.children[0].operation or self.children[0].algorithm == Algos.SORT):
            children_skip = True
        elif self.algorithm == Algos.BITMAP_HEAP_SCAN and self.children[0].algorithm == Algos.BITMAP_INDEX_SCAN:
            children_skip = True
        else:
            children_skip = False

        # recursive
        for child in self.children:
            if self.algorithm == Algos.AGG and len(self.children) > 1 and self.algorithm == Algos.SORT:
                child.to_text(True)
            else:
                child.to_text(children_skip)

        if skip:
            return

        text = ""
        if self.operation == Operations.JOIN:
            if self.algorithm == Algos.HASH_JOIN:
                text = "perform " + self.algorithm + " on "
                for i, child in enumerate(self.children):
                    if i < len(self.children) - 1:
                        text += "table " + child.get_output_name()
                    else:
                        text += " and table " + child.get_output_name()

                text += " under condition " + parse_cond(NodeAttrs.HASH_COND, self.attributes[NodeAttrs.HASH_COND], Node.table_subquery_name_pair)

            elif self.algorithm == Algos.MERGE_JOIN:
                text = "perform " + self.algorithm + " on "
                sort_children = []
                for i, child in enumerate(self.children):
                    if child.algorithm == Algos.SORT:
                        child.set_output_name(
                            child.children[0].get_output_name())
                        sort_children.append(child)
                    if i < len(self.children) - 1:
                        text += "table " + child.get_output_name()
                    else:
                        text += " and table " + child.get_output_name()

                if sort_children:
                    sort_step = "sort "
                    for child in sort_children:
                        if i < len(self.children) - 1:
                            sort_step += ("table " + child.get_output_name())
                        else:
                            sort_step += (" and table " +
                                          child.get_output_name())
                    text = sort_step + " and " + text

        elif self.algorithm == Algos.BITMAP_HEAP_SCAN:
            # combine bitmap heap scan and bitmap index scan
            if self.children[0].algorithm == Algos.BITMAP_INDEX_SCAN and NodeAttrs.RELATION_NAME in self.attributes:
                self.children[0].set_output_name(self.attributes[NodeAttrs.RELATION_NAME])
                text = " with index condition " + parse_cond("Recheck Cond", self.attributes[NodeAttrs.RELATION_NAME], Node.table_subquery_name_pair)

            text = "perform bitmap heap scan on table " + self.children[0].get_output_name() + text

        elif self.operation == Operations.UNIQUE:
            # combine unique and sort
            if self.children[0].operation == Operations.SORT:
                self.children[0].set_output_name(self.children[0].children[0].get_output_name())
                text = "sort " + self.children[0].get_output_name()
                if NodeAttrs.SORT_KEY in self.children[0].attributes:
                    text += " with attribute " + parse_cond("Sort Key", self.children[0].attributes[NodeAttrs.SORT_KEY], Node.table_subquery_name_pair) + " and "
                else:
                    text += " and "

            text += "perform unique on table " + self.children[0].get_output_name()

        elif self.operation == Operations.SCAN:
            if self.algorithm == Algos.SEQ_SCAN:
                text = "perform sequential scan on table "
            else:
                text += "perform " + self.algorithm + " on table "

            text += self.get_output_name()
            if NodeAttrs.INDEX_COND in self.attributes:
                text += " under condition " + parse_cond(NodeAttrs.INDEX_COND, self.attributes[NodeAttrs.INDEX_COND], Node.table_subquery_name_pair)

        elif self.operation == Operations.AGG:
            for child in self.children:
                # combine aggregate and sort
                if child.operation == Operations.SORT:
                    child.set_output_name(child.children[0].get_output_name())
                    text = "sort " + child.get_output_name() + " and "
                # combine aggregate with scan
                if child.operation == Operations.SCAN:
                    if child.algorithm == Algos.SEQ_SCAN:
                        text = "perform sequential scan on " + child.get_output_name() + " and "
                    else:
                        text = "perform " + child.algorithm + " on " + child.get_output_name() + " and "
            text += "perform aggregate on table " + self.children[0].get_output_name()
            if len(self.children) == 2:
                text += " and table " + self.children[1].get_output_name()

        elif self.operation == Operations.SORT:
            text += "perform sort on table " + self.children[0].get_output_name() + " with attribute " + parse_cond(NodeAttrs.SORT_KEY,
                                                                                                                    self.attributes[NodeAttrs.SORT_KEY], Node.table_subquery_name_pair)

        elif self.operation == Operations.LIMIT:
            text = "limit the result from table " + self.children[0].get_output_name() + " to " + str(self.attrs["Plan Rows"]) + " record(s)"

        else:
            text = "perform " + self.algorithm + " on"
            # binary operator
            if self.children:
                for i, child in enumerate(self.children):
                    if i < len(self.children) - 1:
                        text += (" table " + child.get_output_name() + ",")
                    else:
                        text += (" and table " + child.get_output_name())
            # unary operator
            else:
                text += " table " + self.children[0].get_output_name()

        if NodeAttrs.GROUP_KEY in self.attributes:
            text += " with grouping on attribute " + parse_cond("Group Key", self.attributes[NodeAttrs.GROUP_KEY], Node.table_subquery_name_pair)

        if NodeAttrs.FILTER in self.attributes:
            text += " and filtering on " + parse_cond("Table Filter", self.attributes[NodeAttrs.FILTER], Node.table_subquery_name_pair)

        if 'Join Filter' in self.attributes:
            text += " while filtering on " + parse_cond("Join Filter", self.attributes['Join Filter'], Node.table_subquery_name_pair)

        # set intermediate table name
        if increment:
            self.set_output_name("T" + str(Node.cur_table_name))
            text += " to get intermediate table " + self.get_output_name()
            Node.cur_table_name += 1
        if NodeAttrs.SUBPLAN_NAME in self.attributes:
            Node.table_subquery_name_pair[self.attributes[NodeAttrs.SUBPLAN_NAME]] = self.get_output_name()

        self.step = Node.cur_step
        Node.cur_step += 1
        self.text = "Step {}: {}".format(self.step, text)
        Node.steps.append(self.text)

        return self.text
