from apted import APTED, Config

from qepdiff2text.Node import Node

class APTEDConfig(Config):
    def rename(self, node1, node2):
        return 1 if node1.operation != node2.operation else 0

    def children(self, node):
        return node.children

def diff(treeBefore: Node, treeAfter: Node) -> (int, dict):
    """
    Returns the difference between two QEP trees

    :param treeBefore: The 'before tree'.
    :param treeAfter: The 'after tree'.
    :return:
        distance: The structural edit distance between the two trees.
            Only difference in algorithm is captured.
        delta: The difference between the two trees. Has 3 keys:
            - deleted: Those nodes that are deleted from treeBefore
            - inserted: Those nodes that are inserted into treeAfter
            - stayed: Those nodes that are present in both trees. Each entry
                has two keys:

                - before: the node in treeBefore
                - after : the node in treeAfter

                Note that the before and after may be different in attributes
                other than algorithm and operation.
    """
    apted = APTED(treeBefore, treeAfter, APTEDConfig())
    distance = apted.compute_edit_distance()
    mapping = apted.compute_edit_mapping()

    inserted = [m[1] for m in mapping if m[0] is None]
    deleted = [m[0] for m in mapping if m[1] is None]
    stayed = [
        {
            "before": m[0],
            "after": m[1]
        }
        for m in mapping
        if m[0] is not None and m[1] is not None
    ]

    delta = {
        "deleted": deleted,
        "inserted": inserted,
        "stayed": stayed,
    }
    return distance, delta

