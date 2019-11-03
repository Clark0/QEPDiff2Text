from constants import NodeAttrs, Algos, Operations, OP_ALGS

def isOperation(algo, operation):
    return algo in OP_ALGS[operation]

def findOperation(algo):
    for operation in Operations.all():
        if isOperation(algo, operation):
            return operation
    return None

class Node(object):
    def __init__(self, attrs):
        assert isinstance(attrs, dict)
        # assert NodeAttrs.NODE_TYPE in attrs
        self.algorithm = attrs[NodeAttrs.NODE_TYPE]
        self.operation = findOperation(self.algorithm)
        self.attributes = {k: v for k,
                           v in attrs.items() if k in NodeAttrs.all()}

        if self.is_scan():
            if self.algorithm == Algos.INDEX_SCAN:
                if attrs[NodeAttrs.RELATION_NAME]:
                    self.set_output_name(
                        attrs[NodeAttrs.RELATION_NAME] + 
                        " with index " + 
                        attrs[NodeAttrs.INDEX_NAME]
                    )
            elif self.algorithm == Algos.SUBQUERY_SCAN:
                self.set_output_name(attrs[ALIAS])
            else:
                self.set_output_name(attrs[NodeAttrs.RELATION_NAME])

        if NodeAttrs.PLANS in attrs:
            self.children = [Node(child_attrs)
                             for child_attrs in attrs[NodeAttrs.PLANS]]
            self.attributes.pop(NodeAttrs.PLANS)
        else:
            self.children = []

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

    def set_step(self, step):
        self.step = step

    def is_scan(self):
        return self.operation == Operations.SCAN

    def __str__(self, show_algo = False):
        first_line = "- {}".format(self.algorithm if show_algo else self.operation)
        children_lines = [
            "\t" + line 
            for child in self.children
            for line in child.__str__(show_algo).split("\n")
        ]
        return "\n".join([first_line] + children_lines)
