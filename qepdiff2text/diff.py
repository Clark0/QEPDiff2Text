from apted import APTED, Config

from qepdiff2text.Node import Node

class APTEDConfig(Config):
    def rename(self, node1, node2):
        return 1 if node1.operation != node2.operation else 0

    def children(self, node):
        return node.children

def diff(tree_before: Node, tree_after: Node) -> (int, dict):
    """
    Returns the difference between two QEP trees

    :param tree_before: The 'before tree'.
    :param tree_after: The 'after tree'.
    :return:
        distance: The structural edit distance between the two trees.
            Only difference in algorithm is captured.
        delta: The difference between the two trees. Has 3 keys:
            - deleted: Those nodes that are deleted from tree_before
            - inserted: Those nodes that are inserted into tree_after
            - stayed: Those nodes that are present in both trees. Has two
                keys:

                - before: the nodes in tree_before
                - after : the nodes in tree_after

                Note that the before and after may be different in attributes
                other than algorithm and operation.
    """
    apted = APTED(tree_before, tree_after, APTEDConfig())
    distance = apted.compute_edit_distance()
    mapping = apted.compute_edit_mapping()

    delta = {
        "deleted": [m[0] for m in mapping if m[1] is None],
        "inserted": [m[1] for m in mapping if m[0] is None],
        "stayed": {
            "before": [
                m[0]
                for m in mapping
                if m[0] is not None and m[1] is not None
            ],
            "after":[
                m[1]
                for m in mapping
                if m[0] is not None and m[1] is not None
            ]
        }
    }
    return distance, delta

