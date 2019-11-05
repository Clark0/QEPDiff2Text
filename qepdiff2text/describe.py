from .Node import Node
from .Description import\
    InsertionDescription,\
    DeletionDescription,\
    StayedDescription,\
    SameDescription,\
    UpdateDescription

def describe_insertion(node: Node) -> InsertionDescription:
    """
    Returns InsertionDescription object describing an insertion
    :param node: The node inserted
    :return: InsertionDescription object describing an insertion
    """
    return None

def describe_deletion(node: Node) -> DeletionDescription:
    """
    Returns DeletionDescription object describing an deletion
    :param node: The node deleted
    :return: DeletionDescription object describing an deletion
    """
    return None

def describe_stayed(node_before: Node, node_after: Node) -> StayedDescription:
    """
    Returns StayedDescription object describing an stayed node
    :param node_before: The node in tree_before
    :param node_after: The node in tree_after
    :return: StayedDescription object describing an stayed node
    """
    def are_the_same(node_before, node_after) -> bool:
        """
        Returns a bool indicating whether the two nodes are the same
        :param node_before: The node in tree_before
        :param node_after: The node in tree_after
        :return: a bool indicating whether the two nodes are the same
        """
        return True
    if are_the_same(node_before, node_after):
        return describe_same(node_before, node_after)
    else:
        return describe_update(node_before, node_after)
    return None

def describe_same(node_before: Node, node_after: Node) -> SameDescription:
    """
    Returns StayedDescription object describing a node that is the same
    in tree_before and tree_after
    :param node_before: The node in tree_before
    :param node_after: The node in tree_after
    :return: StayedDescription object describing an stayed node
    """
    return None

def describe_update(node_before: Node, node_after: Node) -> UpdateDescription:
    """
    Returns StayedDescription object describing a node that is the updated
    in tree_after
    :param node_before: The node in tree_before
    :param node_after: The node in tree_after
    :return: StayedDescription object describing an stayed node
    """
    return None