from .Node import Node
from .constants import NodeAttrs
from .Description import\
    InsertionDescription,\
    DeletionDescription,\
    StayedDescription,\
    SameDescription,\
    UpdateDescription

interested_attrs = [NodeAttrs.RELATION_NAME, NodeAttrs.GROUP_KEY, NodeAttrs.SORT_KEY,
                            NodeAttrs.JOIN_TYPE, NodeAttrs.INDEX_NAME, NodeAttrs.HASH_COND,
                            NodeAttrs.FILTER, NodeAttrs.INDEX_COND, NodeAttrs.MERGE_COND,
                            NodeAttrs.RECHECK_COND, NodeAttrs.JOIN_FILTER]

# check algorithm ,  then check attributes with #

def describe_insertion(node: Node) -> InsertionDescription:
    """
    Returns InsertionDescription object describing an insertion
    :param node: The node inserted
    :return: InsertionDescription object describing an insertion
    """
    diff = "This node is new in query 2."
    return InsertionDescription("The string inserted", diff)

def describe_deletion(node: Node) -> DeletionDescription:
    """
    Returns DeletionDescription object describing an deletion
    :param node: The node deleted
    :return: DeletionDescription object describing an deletion
    """
    diff = "This node no longer exists in query 2."
    return DeletionDescription("The string deleted", diff)

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

        if node_before.algorithm != node_after.algorithm:
            return False
        elif not _is_output_name_same(node_before, node_after):
            return False
        else:
            for attr in interested_attrs:
                if _exists_attr(attr, node_before, node_after) == 1 or \
                    _exists_attr(attr, node_before, node_after) == 2:
                    return False
                elif _exists_attr(attr, node_before, node_after) == 12 and \
                    node_before.attributes[attr] != node_after.attributes[attr]:
                    return False
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

    # Do nothing
    return SameDescription("Same String1", "Same String2")

def describe_update(node_before: Node, node_after: Node) -> UpdateDescription:
    """
    Returns StayedDescription object describing a node that is the updated
    in tree_after
    :param node_before: The node in tree_before
    :param node_after: The node in tree_after
    :return: StayedDescription object describing an stayed node
    """

    if node_before.algorithm != node_after.algorithm:
        if node_before.operation != node_after.operation:
            diff = "The first query performs " + node_before.algorithm.lower() + \
                   ", but the second one performs " + node_after.algorithm.lower() + "."
        else:
            diff = "Both query perform " + node_before.operation.lower() + \
                   ". However the first query performs "+ node_before.algorithm.lower() + \
                   ', and the second query performs ' + node_after.algorithm.lower() + "."
    else:
        diff = "Both query perform " + node_before.algorithm.lower() + ", but "
        differences = [] # differences between node1 and node2
        node1_special = [] # something node1 has but node2 doesn't have
        node2_special = [] # something node2 has but node1 doesn't have
        if not _is_output_name_same(node_before, node_after):
            differences.append("output name")
        for attr in interested_attrs:
            if _exists_attr(attr, node_before, node_after) == 1:
                differences.append(attr)
                node1_special.append(attr)
            elif _exists_attr(attr, node_before, node_after) == 2:
                differences.append(attr)
                node2_special.append(attr)
            elif _exists_attr(attr, node_before, node_after) == 12 and \
                node_before.attributes[attr] != node_after.attributes[attr]:
                differences.append(attr)
        differences = [d.lower() for d in differences]
        if len(differences) == 1:
            diff += differences[0] + " is different. "
        else:
            diff += ", ".join(differences[:-1])
            diff += " and " + differences[-1] + " are different. "

        node1_special = [s1.lower() for s1 in node1_special]
        node2_special = [s2.lower() for s2 in node2_special]
        if len(node1_special) == 1:
            diff += "Query 1 has " + node1_special[0] + ", but query 2 doesn't have. "
            if len(node1_special) > 1:
                diff += "Query 1 has " + ", ".join(node1_special[:-1]) + \
                        " and " + node1_special[-1] +", but query 2 doesn't have. "

        if len(node2_special) == 1:
            diff += "Query 2 has " + node2_special[0] + ", but query 1 doesn't have. "
            if len(node2_special) > 1:
                diff += "Query 2 has " + ", ".join(node2_special[:-1]) + \
                        " and " + node2_special[-1] + ", but query 1 doesn't have. "

    return UpdateDescription("Before String", "After String", diff)

def _is_output_name_same(node_before: Node, node_after: Node) -> bool:
    # Outname doesn't start with "T" are ALIAS given by User. If 2 ALIAS are different,
    # 2 nodes are considered as different. If 2 nodes both start with "T",
    # we don't care about the digit after "T"
    if node_before.get_output_name() != node_after.get_output_name() \
            and (node_before.get_output_name()[0] != "T"
                 or node_after.get_output_name()[0] != "T"):
        return False  # Output name are different
    else:
        return True # Output name are same

def _exists_attr(attr: str, node_1: Node, node_2: Node) -> int:
    # return 12 if attributes in both nodes,
    # return 1 if attributes in node 1,
    # return 2 if attributes in node 2,
    # return 0 if attributes not in node 1 or 2.
    if attr in node_1.attributes and attr in node_2.attributes:
        return 12 # attributes exist in both nodes
    elif attr in node_1.attributes:
        return 1 # attributes exist in node 1
    elif attr in node_2.attributes:
        return 2  # attributes exist in node 2
    else:
        return 0 # attributes don't exist on both node