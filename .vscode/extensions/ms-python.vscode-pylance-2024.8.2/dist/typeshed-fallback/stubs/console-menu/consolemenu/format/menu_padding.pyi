class MenuPadding:
    def __init__(self, top: int = 1, left: int = 2, bottom: int = 1, right: int = 2) -> None: ...
    @property
    def left(self) -> int: ...
    @left.setter
    def left(self, left: int) -> None: ...
    @property
    def right(self) -> int: ...
    @right.setter
    def right(self, right: int) -> None: ...
    @property
    def top(self) -> int: ...
    @top.setter
    def top(self, top: int) -> None: ...
    @property
    def bottom(self) -> int: ...
    @bottom.setter
    def bottom(self, bottom: int) -> None: ...
