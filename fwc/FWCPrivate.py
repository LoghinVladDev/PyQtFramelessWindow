from enum import Enum

from abc import abstractmethod

from __future__ import annotations


class FramelessWindowConverter:
    pass


class FWCBorderHitTestResult(Enum):
    TOP_LEFT        = 1
    TOP             = 2
    TOP_RIGHT       = 3
    RIGHT           = 4
    BOTTOM_RIGHT    = 5
    BOTTOM          = 6
    BOTTOM_LEFT     = 7
    LEFT            = 8
    CLIENT          = 9
    NONE            = 10


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


class FWCPoint:
    def __init__(self, x: int, y: int):
        self.__x: int = x
        self.__y: int = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        self.__x = value

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, value: int) -> None:
        self.__y = value


class FWCPointF:
    def __init__(self, x: float, y: float):
        self.__x: float = x
        self.__y: float = y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, value: float) -> None:
        self.__x = value

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, value: float) -> None:
        self.__y = value


class FramelessWindowConverterPrivate:
    @staticmethod
    def create(p: FramelessWindowConverter) -> FramelessWindowConverterPrivate:
        pass

    def __init__(self, p: FramelessWindowConverter):
        self.__q: FramelessWindowConverter  = p
        self.__fullscreen: bool             = False

    @abstractmethod
    def filter_native_event(self, message: bytes, result: int) -> bool:
        ...

    @abstractmethod
    def convert_to_frameless(self) -> None:
        ...

    @abstractmethod
    def convert_to_window_with_frame(self) -> None:
        ...

    def hide_for_translucency(self) -> None:
        pass

    def show_for_translucency(self) -> None:
        pass

    @abstractmethod
    def minimize_window(self) -> None:
        ...

    @abstractmethod
    def maximize_window(self) -> None:
        ...

    @abstractmethod
    def close_window(self) -> None:
        ...

    @abstractmethod
    def restore_window(self) -> None:
        ...

    @abstractmethod
    def toggle_fullscreen(self) -> None:
        ...

    def set_enable_shadow(self) -> None:
        pass

    def set_hidden_green_traffic_light(self, value: bool) -> None:
        pass

    def set_hidden_yellow_traffic_light(self, value: bool) -> None:
        pass

    def set_hidden_red_traffic_light(self, value: bool) -> None:
        pass

    def set_enabled_green_traffic_light(self, value: bool) -> None:
        pass

    def set_enabled_yellow_traffic_light(self, value: bool) -> None:
        pass

    def set_enabled_red_traffic_light(self, value: bool) -> None:
        pass

    def set_horizontal_alignment_of_traffic_lights(self) -> None:
        pass

    def set_x_position_of_traffic_lights(self) -> None:
        pass

    def set_y_position_of_traffic_lights(self) -> None:
        pass

    def do_border_hit_test(
            self,
            window_rect: FWCRect,
            mouse_position: FWCPoint,
            border_width: int
    ) -> FWCBorderHitTestResult:
        pass
