from constants import NodeAttrs


class Node(object):
    def __init__(self, attrs):
        assert isinstance(attrs, dict)
        # assert NodeAttrs.NODE_TYPE in attrs
        self.node_type = attrs[NodeAttrs.NODE_TYPE]
        self.attributes = {k: v for k,
                           v in attrs.items() if k in NodeAttrs.all()}

        if NodeAttrs.PLANS in attrs:
            self.children = [Node(child_attrs)
                             for child_attrs in attrs[NodeAttrs.PLANS]]
            self.attributes.pop(NodeAttrs.PLANS)
        else:
            self.children = None

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
