from . import StayedDescription


class SameDescription(StayedDescription):
    """
        SameDescription contains the description of a node that is the same
        in both 'before tree' and 'after tree'.

        Attributes:
            before_des (str): the description of the the node in the 'before tree'.
            after_des (str): the description of the the node in the 'after tree'.
    """

    def __init__(self, before_des: str, after_des: str):
        StayedDescription.__init__(self, before_des, after_des)
