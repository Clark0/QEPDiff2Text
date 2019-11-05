from typing import List

from qepdiff2text.Node import Node
from qepdiff2text.diff import diff
from qepdiff2text.Description import Description


def get_des(treeBefore: Node, treeAfter: Node) -> List[Description]:
    """
    Generates the description of difference between the two trees.

    :param treeBefore: The 'before tree'.
    :param treeAfter: The 'after tree'.
    :return: A list of Descriptions.
    """
    distance, delta = diff(treeBefore, treeAfter)
    return []