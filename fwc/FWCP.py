from __future__ import annotations

from enum import Enum

from abc import abstractmethod

from ctypes import c_long   as c_sint32
from ctypes import c_void_p as c_void_pointer
from ctypes import pointer  as c_address_of
from ctypes import POINTER  as c_pointer

import fwc_types
import fwc


class FWCP:
    @staticmethod
    def create(p: fwc.FWC.FWC) -> fwc.FWCP.FWCP:
        pass

    def __init__(self, p: fwc.FWC.FWC):
        self.__q: fwc.FWC.FWC               = p
        self.__fullscreen: bool             = False

    @property
    def fullscreen(self) -> bool:
        return self.__fullscreen

    @fullscreen.setter
    def fullscreen(self, value: bool) -> None:
        self.__fullscreen = value

    @property
    def q(self) -> fwc.FWC.FWC:
        return self.__q

    @q.setter
    def q(self, value: fwc.FWC.FWC):
        self.__q = value

    @abstractmethod
    def filter_native_event(self, message: c_void_pointer, result: c_pointer(c_sint32)) -> bool:
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
            window_rect: fwc_types.FWCRect.FWCRect,
            mouse_position: fwc_types.FWCPoint.FWCPoint,
            border_width: int
    ) -> fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult:
        pass
