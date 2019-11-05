from . import StayedDescription
from . import DescriptionWithDiff

class UpdateDescription(StayedDescription, DescriptionWithDiff):
    """
        UpdateDescription contains the description of of a node in 'before tree', description
        of that node(updated) in the 'after tree' and the difference between the two trees

        Attributes:
            before_des (str): the description of the the node inserted in the 'before tree'.
            after_des (str): the description of the the node inserted in the 'after tree'.
            diff_des (str): the description of the difference.
    """
    def __init__(self, before_des: str, after_des: str, diff_des: str):
        StayedDescription.__init__(self, before_des, after_des)
        DescriptionWithDiff.__init__(self, diff_des)
