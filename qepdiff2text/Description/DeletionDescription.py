from . import DescriptionWithBefore
from . import DescriptionWithDiff

class DeletionDescription(DescriptionWithBefore, DescriptionWithDiff):
    """
        DeletionDescription contains the description of a nodes that is deleted
        from the first tree.

        Attributes:
            before_des (str): the description of the the node deleted in the 'before tree'.
            diff_des (str): the description of the difference.
    """
    def __init__(self, before_des: str, diff_des: str):
        DescriptionWithBefore.__init__(self, before_des)
        DescriptionWithDiff.__init__(self, diff_des)
