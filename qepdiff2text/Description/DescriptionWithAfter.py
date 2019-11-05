from . import Description

class DescriptionWithAfter(Description):
    """
        DescriptionWithAfter is a contains the description of the node in
        the 'after tree'.

        Attributes:
            after_des (str): the description of the node in the 'after tree'.
    """
    def __init__(self, after_des: str) -> None:
        Description.__init__(self)
        self.after_des: str = after_des

    def get_after_des(self) -> str:
        return self.after_des

    def set_after_des(self, after_des: str) -> None:
        self.after_des: str = after_des
