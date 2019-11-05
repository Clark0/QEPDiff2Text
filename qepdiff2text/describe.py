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

def describe_stayed(nodeBefore: Node, nodeAfter: Node) -> StayedDescription:
    """
    Returns StayedDescription object describing an stayed node
    :param nodeBefore: The node in tree_before
    :param nodeAfter: The node in tree_after
    :return: StayedDescription object describing an stayed node
    """
    def are_the_same(nodeBefore, nodeAfter) -> bool:
        """
        Returns a bool indicating whether the two nodes are the same
        :param nodeBefore: The node in tree_before
        :param nodeAfter: The node in tree_after
        :return: a bool indicating whether the two nodes are the same
        """
        return True
    if are_the_same(nodeBefore, nodeAfter):
        return describe_same(nodeBefore, nodeAfter)
    else:
        return describe_update(nodeBefore, nodeAfter)
    return None

def describe_same(nodeBefore: Node, nodeAfter: Node) -> SameDescription:
    """
    Returns StayedDescription object describing a node that is the same
    in tree_before and tree_after
    :param nodeBefore: The node in tree_before
    :param nodeAfter: The node in tree_after
    :return: StayedDescription object describing an stayed node
    """
    return None

def describe_update(nodeBefore: Node, nodeAfter: Node) -> UpdateDescription:
    """
    Returns StayedDescription object describing a node that is the updated
    in tree_after
    :param nodeBefore: The node in tree_before
    :param nodeAfter: The node in tree_after
    :return: StayedDescription object describing an stayed node
    """
    return None