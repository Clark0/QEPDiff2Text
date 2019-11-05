from typing import List, Iterator

from . import describe
from .diff import diff
from .utils import post_order_tree_traversal, infinite_none_suffix
from .Node import Node
from .Description import Description

def get_des(tree_before: Node, tree_after: Node) -> List[Description]:
    """
    Generates the description of difference between the two trees.

    :param tree_before: The 'before tree'.
    :param tree_after: The 'after tree'.
    :return: A list of Descriptions.
    """

    des_gen: Iterator[Description] = get_des_gen(tree_before, tree_after)

    return list(des_gen)

def get_des_gen(tree_before: Node, tree_after: Node) -> Iterator[Description]:
    """
    Returns a generator of the descriptions of difference between the two trees.

    :param tree_before: The 'before tree'.
    :param tree_after: The 'after tree'.
    :return: A list of Descriptions.
    """
    distance, delta = diff(tree_before, tree_after)

    tree_before_iter: Iterator[Node] = infinite_none_suffix(
        post_order_tree_traversal(tree_before)
    )
    tree_after_iter: Iterator[Node] = infinite_none_suffix(
        post_order_tree_traversal(tree_after)
    )

    cur_node_before: Node = next(tree_before_iter)
    cur_node_after: Node = next(tree_after_iter)

    while cur_node_before or cur_node_after:
        while cur_node_after in delta['inserted']:
            yield describe.describe_deletion(cur_node_after)
            cur_node_after = next(tree_after_iter)
        while cur_node_before in delta['deleted']:
            yield describe.describe_deletion(cur_node_before)
            cur_node_before = next(tree_before_iter)
        while cur_node_before in delta['stayed']['before']:
            yield describe.describe_stayed(cur_node_before, cur_node_after)
            cur_node_before = next(tree_before_iter)
            cur_node_after = next(tree_after_iter)
    return