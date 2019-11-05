from . import Description

class DescriptionWithDiff(Description):
    """
        DescriptionWithDiff is a contains the description of the difference
        between two nodes.

        Attributes:
            diff_des (str): the description of the difference between two nodes.
    """
    def __init__(self, diff_des: str) -> None:
        Description.__init__(self)
        self.diff_des: str = diff_des

    def get_diff_des(self) -> str:
        return self.diff_des

    def set_diff_des(self, diff_des: str) -> None:
        self.diff_des: str = diff_des
