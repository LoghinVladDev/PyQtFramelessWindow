from abc import abstractmethod
from typing import Callable

from .FWCPrivate import FramelessWindowConverterPrivate


# noinspection PyTypeChecker
class FWC:
    def __init__(self):
        self.__d_ptr: FramelessWindowConverterPrivate                   = None
        self.__window_handle: int                                       = 0

        self.__should_perform_window_drag: Callable[[int, int], bool]   = lambda x, y: True
        self.__release_mouse_grab: Callable[[None], None]               = lambda: None

        self.__border_width: int                                        = 0

        self.__minimum_window_width: int                                = 0
        self.__minimum_window_height: int                               = 0
        self.__maximum_window_width: int                                = 0
        self.__maximum_window_height: int                               = 0

        self.__use_traffic_lights: bool                                 = False
        self.__is_frameless: bool                                       = False
        self.__has_shadow: bool                                         = False
        self.__enable_resizing: bool                                    = False

        # macOS Settings

        self.__hidden_green: bool                                       = False
        self.__hidden_red: bool                                         = False
        self.__hidden_yellow: bool                                      = False

        self.__enabled_green: bool                                      = True
        self.__enabled_red: bool                                        = True
        self.__enabled_yellow: bool                                     = True

        self.__traffic_lights_alignment_horizontal: bool                = True
        self.__x_pos_of_traffic_lights: int                             = 7
        self.__y_pos_of_traffic_lights: int                             = 3

    def filter_native_events(self, message: bytes, result: int) -> bool:
        pass

    def convert_window_to_frameless(self, window_handle: int, release_mouse_grab: Callable[[None], None] = lambda: None) -> None:
        pass

    def toggle_window_frame_after_conversion(self) -> None:
        pass

    def get_is_frameless(self) -> bool:
        pass

    @property
    def window_handle(self) -> int:
        return self.__window_handle

    @property
    def should_perform_window_drag(self) -> Callable[[int, int], bool]:
        return self.__should_perform_window_drag

    @should_perform_window_drag.setter
    def should_perform_window_drag(self, value: Callable[[int, int], bool]) -> None:
        self.__should_perform_window_drag = value

    @property
    def release_mouse_grab(self) -> Callable[[None], None]:
        return self.__release_mouse_grab

    @release_mouse_grab.setter
    def release_mouse_grab(self, value: Callable[[None], None]) -> None:
        self.__release_mouse_grab = value

    @property
    def border_width(self) -> int:
        return self.__border_width

    @border_width.setter
    def border_width(self, value: int) -> None:
        self.__border_width = value

    @property
    def enable_resizing(self) -> bool:
        return self.__enable_resizing

    @enable_resizing.setter
    def enable_resizing(self, value: bool) -> None:
        self.__enable_resizing = value

    @property
    def minimum_window_width(self) -> int:
        return self.__minimum_window_width

    @minimum_window_width.setter
    def minimum_window_width(self, value: int) -> None:
        self.__minimum_window_width = value

    @property
    def maximum_window_width(self) -> int:
        return self.__maximum_window_width

    @maximum_window_width.setter
    def maximum_window_width(self, value: int) -> None:
        self.__maximum_window_width = value

    @property
    def minimum_window_height(self) -> int:
        return self.__minimum_window_height

    @minimum_window_height.setter
    def minimum_window_height(self, value: int) -> None:
        self.__minimum_window_height = value

    @property
    def maximum_window_height(self) -> int:
        return self.__maximum_window_height

    @maximum_window_height.setter
    def maximum_window_height(self, value: int) -> None:
        self.__maximum_window_height = value

    def set_min_max_window_sizes(self, min_width: int, min_height: int, max_width: int, max_height: int) -> None:
        self.minimum_window_width = min_width
        self.minimum_window_height = min_height
        self.maximum_window_width = max_width
        self.maximum_window_height = max_height

    def hide_for_translucency(self) -> None:
        pass

    def show_for_translucency(self) -> None:
        pass

    def minimize_window(self) -> None:
        pass

    def maximize_window(self) -> None:
        pass

    def restore_window(self) -> None:
        pass

    def close_window(self) -> None:
        pass

    def toggle_fullscreen(self) -> None:
        pass

    @property
    def has_shadow(self) -> bool:
        return self.__has_shadow

    @has_shadow.setter
    def has_shadow(self, value: bool) -> None:
        self.__has_shadow = value

    @property
    def use_traffic_lights(self) -> bool:
        return self.__use_traffic_lights

    @use_traffic_lights.setter
    def use_traffic_lights(self, value: bool) -> None:
        self.__use_traffic_lights = value

    @property
    def hidden_green_traffic_light(self) -> bool:
        return self.__hidden_green

    @hidden_green_traffic_light.setter
    def hidden_green_traffic_light(self, value: bool) -> None:
        self.__hidden_green = value

    @property
    def hidden_yellow_traffic_light(self) -> bool:
        return self.__hidden_yellow

    @hidden_yellow_traffic_light.setter
    def hidden_yellow_traffic_light(self, value: bool) -> None:
        self.__hidden_yellow = value

    @property
    def hidden_red_traffic_light(self) -> bool:
        return self.__hidden_red

    @hidden_red_traffic_light.setter
    def hidden_red_traffic_light(self, value: bool) -> None:
        self.__hidden_red = value

    @property
    def enabled_green_traffic_light(self) -> bool:
        return self.__enabled_green

    @enabled_green_traffic_light.setter
    def enabled_green_traffic_light(self, value: bool) -> None:
        self.__enabled_green = value

    @property
    def enabled_yellow_traffic_light(self) -> bool:
        return self.__enabled_yellow

    @enabled_yellow_traffic_light.setter
    def enabled_yellow_traffic_light(self, value: bool) -> None:
        self.__enabled_yellow = value

    @property
    def enabled_red_traffic_light(self) -> bool:
        return self.__enabled_red

    @enabled_red_traffic_light.setter
    def enabled_red_traffic_light(self, value: bool) -> None:
        self.__enabled_red = value

    @property
    def horizontal_alignment_of_traffic_lights(self) -> bool:
        return self.__traffic_lights_alignment_horizontal

    @horizontal_alignment_of_traffic_lights.setter
    def horizontal_alignment_of_traffic_lights(self, value: bool) -> None:
        self.__traffic_lights_alignment_horizontal = value

    @property
    def x_position_of_traffic_lights(self) -> int:
        return self.__x_pos_of_traffic_lights

    @x_position_of_traffic_lights.setter
    def x_position_of_traffic_lights(self, value: int) -> None:
        self.__x_pos_of_traffic_lights = value

    @property
    def y_position_of_traffic_lights(self) -> int:
        return self.__y_pos_of_traffic_lights

    @y_position_of_traffic_lights.setter
    def y_position_of_traffic_lights(self, value: int) -> None:
        self.__y_pos_of_traffic_lights = value