from . import DescriptionWithBefore
from . import DescriptionWithAfter

class SameDescription(DescriptionWithBefore, DescriptionWithAfter):
    """
        SameDescription contains the description of two nodes that are the same.

        Attributes:
            before_des (str): the description of the the node in the 'before tree'.
            after_des (str): the description of the the node in the 'after tree'.
    """
    def __init__(self, before_des: str, after_des: str):
        DescriptionWithBefore.__init__(self, before_des)
        DescriptionWithAfter.__init__(self, after_des)
