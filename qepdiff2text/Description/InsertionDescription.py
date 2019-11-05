from . import DescriptionWithAfter
from . import DescriptionWithDiff

class InsertionDescription(DescriptionWithAfter, DescriptionWithDiff):
    """
        InsertionDescription contains the description of a nodes that is deleted
        from the first tree.

        Attributes:
            after_des (str): the description of the the node inserted in the 'after tree'.
            diff_des (str): the description of the difference.
    """
    def __init__(self, after_des: str, diff_des: str):
        DescriptionWithAfter.__init__(self, after_des)
        DescriptionWithDiff.__init__(self, diff_des)
