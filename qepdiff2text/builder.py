import node


def build_node(attrs):
    assert isinstance(attrs, dict) and 'Node type' in attrs
    args = attrs.copy()
    return node(**args)
