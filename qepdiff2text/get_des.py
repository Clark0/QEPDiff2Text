from typing import List

from . import describe
from .diff import diff
from .utils import post_order_tree_traversal

def get_des(tree_before: Node, tree_after: Node) -> List[Description]:
    """
    Generates the description of difference between the two trees.

    :param tree_before: The 'before tree'.
    :param tree_after: The 'after tree'.
    :return: A list of Descriptions.
    """
    distance, delta = diff(tree_before, tree_after)
    return []