from . import DescriptionWithBefore
from . import DescriptionWithAfter
from . import DescriptionWithDiff

class UpdateDescription(DescriptionWithBefore, DescriptionWithAfter, DescriptionWithDiff):
    """
        UpdateDescription contains the description of of a node in 'before tree', description
        of the node edited in the 'after tree' and the difference between the two trees

        Attributes:
            before_des (str): the description of the the node inserted in the 'before tree'.
            after_des (str): the description of the the node inserted in the 'after tree'.
            diff_des (str): the description of the difference.
    """
    def __init__(self, before_des: str, after_des: str, diff_des: str):
        DescriptionWithBefore.__init__(self, before_des)
        DescriptionWithAfter.__init__(self, after_des)
        DescriptionWithDiff.__init__(self, diff_des)
