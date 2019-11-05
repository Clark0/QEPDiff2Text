from . import Description

class DescriptionWithBefore(Description):
    """
        DescriptionWithBefore is a contains the description of the node in
        the 'before tree'.

        Attributes:
            before_des (str): the description of the node in the 'before tree'.
    """
    def __init__(self, before_des: str) -> None:
        Description.__init__(self)
        self.before_des: str = before_des

    def get_before_des(self) -> str:
        return self.before_des

    def set_before_des(self, before_des: str) -> None:
        self.before_des: str = before_des
