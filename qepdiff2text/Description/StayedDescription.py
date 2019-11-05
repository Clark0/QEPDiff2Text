from . import DescriptionWithBefore
from . import DescriptionWithAfter

class StayedDescription(DescriptionWithBefore, DescriptionWithAfter):
    """
        StayedDescription contains the description of a nodes that is present
        in both 'before tree' and 'after tree'.

        Attributes:
            before_des (str): the description of the the node in the 'before tree'.
            after_des (str): the description of the the node in the 'after tree'.
    """
    def __init__(self, before_des: str, after_des: str):
        DescriptionWithBefore.__init__(self, before_des)
        DescriptionWithAfter.__init__(self, after_des)
