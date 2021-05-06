class FWCRect:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    @property
    def left(self) -> int:
        return self.__x1

    @left.setter
    def left(self, value: int) -> None:
        self.__x1 = value

    @property
    def right(self) -> int:
        return self.__x2

    @right.setter
    def right(self, value: int) -> None:
        self.__x2 = value

    @property
    def top(self) -> int:
        return self.__y1

    @top.setter
    def top(self, value: int) -> None:
        self.__y1 = value

    @property
    def bottom(self) -> int:
        return self.__y2

    @bottom.setter
    def bottom(self, value: int) -> None:
        self.__y2 = value


