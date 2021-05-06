import sys

if sys.platform.startswith('win'):
    from enum import Enum

    import fwc
    import fwc_types

    from ctypes import c_void_p as          c_void_pointer
    from ctypes import c_long as            c_sint32
    from ctypes import pointer as           c_address_of
    from ctypes import POINTER as           c_pointer

    from ctypes.wintypes import HWND as     winapi_window_handle
    from ctypes.wintypes import LPARAM as   winapi_lparam

    from ctypes import c_ulonglong as       c_uint64
    from ctypes import c_longlong as        c_sint64
    from ctypes import c_int as             c_sint32
    from ctypes import cast as              static_cast

    from ctypes.wintypes import WORD as     winapi_word_uint16
    from ctypes.wintypes import LPWSTR as   winapi_wchar_pointer
    from ctypes.wintypes import PDWORD as   winapi_dword_uint32_pointer
    from ctypes.wintypes import PULONG as   winapi_uint32_pointer
    from ctypes.wintypes import PLONG as    winapi_sint32_pointer
    from ctypes.wintypes import RECT as     winapi_RECT
    from ctypes.wintypes import LONG as     winapi_sint32

    from ctypes.wintypes import MSG as      winapi_MSG

    from ctypes.wintypes import POINT as    winapi_POINT

    winapi_lresult = winapi_sint32_pointer

    from ctypes import byref

    from ..platform.win.func.GetWindowLongPtrW import GetWindowLongPtrW as \
        winapi_get_window_long_ptr_w
    from ..platform.win.func.GetWindowLongPtrW import GetWindowLongOption as \
        winapi_GetWindowLongPtrOption
    from ..platform.win.func.SetWindowLongPtrW import SetWindowLongPtrW as \
        winapi_set_window_long_ptr_w
    from ..platform.win.func.ShowWindow import ShowWindow as \
        winapi_show_window
    from ..platform.win.func.ShowWindow import ShowWindowOption as \
        winapi_ShowWindowOption
    from ..platform.win.func.SendMessage import SendMessage as \
        winapi_send_message
    from ..platform.win.WindowMessage import WindowMessage as \
        winapi_WindowMessage
    from ..platform.win.WindowStyle import WindowStyle as \
        winapi_WindowStyle
    from ..platform.win.func.DwmExtendFrameIntoClientArea import MARGINS as \
        winapi_MARGINS
    from ..platform.win.func.DwmExtendFrameIntoClientArea import DwmExtendFrameIntoClientArea as \
        winapi_dwm_extend_frame_into_client_area
    from ..platform.win.func.SetWindowPos import SetWindowPos as \
        winapi_set_window_position
    from ..platform.win.func.SetWindowPos import SetWindowPosOption as \
        winapi_SetWindowPositionOption
    from ..platform.win.func.GetClientRect import GetClientRect as \
        winapi_get_client_rect
    from ..platform.win.func.GetWindowRect import GetWindowRect as \
        winapi_get_window_rect
    from ..platform.win.func.GetWindowPlacement import GetWindowPlacement as \
        winapi_get_window_placement
    from ..platform.win.func.GetWindowPlacement import WINDOWPLACEMENT as \
        winapi_WINDOWPLACEMENT


    def u_long_low(long: c_uint64) -> winapi_word_uint16:
        return static_cast(static_cast(long.value, winapi_dword_uint32_pointer).value & 0xffff, winapi_word_uint16)


    def long_low(long: c_sint64) -> winapi_word_uint16:
        return static_cast(static_cast(long.value, winapi_dword_uint32_pointer).value & 0xffff, winapi_word_uint16)


    def u_long_high(long: c_uint64) -> winapi_word_uint16:
        return static_cast((static_cast(long.value, winapi_dword_uint32_pointer).value >> 16) & 0xffff,
                           winapi_word_uint16)


    def long_high(long: c_sint64) -> winapi_word_uint16:
        return static_cast((static_cast(long.value, winapi_dword_uint32_pointer).value >> 16) & 0xffff,
                           winapi_word_uint16)


    class CursorNames(Enum):
        WEST_EAST = 0x01
        NORTH_SOUTH = 0x02
        NORTH_EAST_SOUTH_WEST = 0x04
        NORTH_WEST_SOUTH_EAST = 0x08
        ARROW = 0x10


    def get_cursor_resource(cursor_name: CursorNames) -> winapi_wchar_pointer:
        if cursor_name == CursorNames.WEST_EAST:
            return static_cast(static_cast(static_cast(32644, winapi_word_uint16).value, winapi_uint32_pointer).value,
                               winapi_wchar_pointer)
        elif cursor_name == CursorNames.NORTH_SOUTH:
            return static_cast(static_cast(static_cast(32645, winapi_word_uint16).value, winapi_uint32_pointer).value,
                               winapi_wchar_pointer)
        elif cursor_name == CursorNames.NORTH_EAST_SOUTH_WEST:
            return static_cast(static_cast(static_cast(32643, winapi_word_uint16).value, winapi_uint32_pointer).value,
                               winapi_wchar_pointer)
        elif cursor_name == CursorNames.NORTH_WEST_SOUTH_EAST:
            return static_cast(static_cast(static_cast(32642, winapi_word_uint16).value, winapi_uint32_pointer).value,
                               winapi_wchar_pointer)
        elif cursor_name == CursorNames.ARROW:
            return static_cast(static_cast(static_cast(32512, winapi_word_uint16).value, winapi_uint32_pointer).value,
                               winapi_wchar_pointer)
        else:
            return static_cast(0, winapi_wchar_pointer)


    class FWCWindows(fwc.FWCP):
        class Style(Enum):
            WINDOWED = winapi_WindowStyle.WS_OVERLAPPEDWINDOW.value | \
                       winapi_WindowStyle.WS_THICKFRAME.value | \
                       winapi_WindowStyle.WS_CAPTION.value | \
                       winapi_WindowStyle.WS_SYSMENU.value | \
                       winapi_WindowStyle.WS_MINIMIZEBOX.value | \
                       winapi_WindowStyle.WS_MAXIMIZEBOX.value
            AERO_BORDERLESS = winapi_WindowStyle.WS_POPUP.value | \
                              winapi_WindowStyle.WS_THICKFRAME.value | \
                              winapi_WindowStyle.WS_SYSMENU.value | \
                              winapi_WindowStyle.WS_MINIMIZEBOX.value | \
                              winapi_WindowStyle.WS_MAXIMIZEBOX.value
            MAXIMIZED_BORDERLESS = winapi_WindowStyle.WS_POPUP.value | \
                                   winapi_WindowStyle.WS_THICKFRAME.value

        def __init__(self, q: fwc.FWC.FWC):
            super().__init__(q)

            self.__handle: winapi_window_handle = winapi_window_handle(0)

        def convert_to_frameless(self) -> None:
            self.__handle: winapi_window_handle = static_cast(super().q.window_handle, winapi_window_handle)
            super().set_frameless(True)

        def convert_to_window_with_frame(self) -> None:
            super().set_frameless(False)

        def minimize_window(self) -> None:
            if not super().fullscreen:
                winapi_set_window_long_ptr_w(
                    self.__handle,
                    winapi_GetWindowLongPtrOption.GWL_STYLE.value,
                    winapi_get_window_long_ptr_w(
                        self.__handle,
                        winapi_GetWindowLongPtrOption.GWL_STYLE.value
                    ).value | winapi_WindowStyle.WS_CAPTION.value
                )

                winapi_show_window(
                    self.__handle,
                    winapi_ShowWindowOption.SW_MINIMIZE.value
                )

        def maximize_window(self) -> None:
            winapi_show_window(
                self.__handle,
                winapi_ShowWindowOption.SW_MAXIMIZE.value
            )

        def restore_window(self) -> None:
            winapi_show_window(
                self.__handle,
                winapi_ShowWindowOption.SW_RESTORE.value
            )

        def close_window(self) -> None:
            winapi_send_message(
                self.__handle,
                winapi_WindowMessage.WM_CLOSE.value,
                0, 0
            )

        def toggle_fullscreen(self) -> None:
            super().fullscreen = not super().fullscreen
            if super().fullscreen:
                winapi_show_window(
                    self.__handle,
                    winapi_ShowWindowOption.SW_RESTORE
                )

                winapi_show_window(
                    self.__handle,
                    winapi_ShowWindowOption.SW_MAXIMIZE
                )
            else:
                winapi_show_window(
                    self.__handle,
                    winapi_ShowWindowOption.SW_RESTORE
                )

        def set_enable_shadow(self) -> None:
            shadow: winapi_MARGINS

            if super().q.has_shadow:
                shadow: winapi_MARGINS = winapi_MARGINS(1, 1, 1, 1)
            else:
                shadow: winapi_MARGINS = winapi_MARGINS(0, 0, 0, 0)

            winapi_dwm_extend_frame_into_client_area(self.__handle, byref(shadow))

            winapi_set_window_position(
                self.__handle,
                None,
                0, 0, 0, 0,
                winapi_SetWindowPositionOption.SWP_FRAMECHANGED.value |
                winapi_SetWindowPositionOption.SWP_NOMOVE.value |
                winapi_SetWindowPositionOption.SWP_NOSIZE.value
            )

            winapi_show_window(
                self.__handle,
                winapi_ShowWindowOption.SW_SHOW.value
            )

        def get_current_client_rect(self) -> fwc_types.FWCRect.FWCRect:
            win_rect: winapi_RECT = winapi_RECT()
            if not winapi_get_client_rect(self.__handle, byref(win_rect)):
                return fwc_types.FWCRect.FWCRect(-1, -1, -1, -1)
            return fwc_types.FWCRect.FWCRect(
                win_rect.left.value,
                win_rect.top.value,
                win_rect.right.value,
                win_rect.bottom.value
            )

        def get_current_window_rect(self) -> fwc_types.FWCRect.FWCRect:
            win_rect: winapi_RECT = winapi_RECT()
            if not winapi_get_window_rect(self.__handle, byref(win_rect)):
                return fwc_types.FWCRect.FWCRect(-1, -1, -1, -1)
            return fwc_types.FWCRect.FWCRect(
                win_rect.left.value,
                win_rect.top.value,
                win_rect.right.value,
                win_rect.bottom.value
            )

        def get_current_mouse_pos(self, param: winapi_lparam) -> fwc_types.FWCPoint.FWCPoint:
            return fwc_types.FWCPoint.FWCPoint(long_low(param).value, long_high(param).value)

        def filter_native_event(self, message: c_void_pointer, result: c_pointer(c_sint32)):
            message: c_pointer(winapi_MSG) = static_cast(message, c_pointer(winapi_MSG))

            if message.contents.message.value == winapi_WindowMessage.WM_NCCALCSIZE.value:
                if message.contents.wParam:
                    result.contents.value = 0
                    return True
            elif message.contents.message.value == winapi_WindowMessage.WM_WINDOWPOSCHANGING.value:
                window_placement: winapi_WINDOWPLACEMENT = winapi_WINDOWPLACEMENT(
                    0, 0, 0,
                    winapi_POINT(0, 0), winapi_POINT(0, 0),
                    winapi_RECT(0, 0, 0, 0),
                    winapi_RECT(0, 0, 0, 0)
                )
                winapi_get_window_placement(self.__handle, byref(window_placement))

                if window_placement.showCmd.value != winapi_ShowWindowOption.SW_SHOWMAXIMIZED.value and \
                        not (
                            winapi_get_window_long_ptr_w(
                                self.__handle,
                                winapi_GetWindowLongPtrOption.GWL_STYLE.value
                            ).value & winapi_WindowStyle.WS_SYSMENU.value
                        ):
                    winapi_set_window_long_ptr_w(
                        self.__handle,
                        winapi_GetWindowLongPtrOption.GWL_STYLE.value,
                        static_cast(FWCWindows.Style.AERO_BORDERLESS.value, winapi_sint32)
                    )

                    winapi_set_window_position(
                        self.__handle,
                        None,
                        0, 0, 0, 0,
                        winapi_SetWindowPositionOption.SWP_FRAMECHANGED.value   |
                        winapi_SetWindowPositionOption.SWP_NOMOVE.value         |
                        winapi_SetWindowPositionOption.SWP_NOSIZE.value
                    )

                    winapi_show_window(
                        self.__handle,
                        winapi_ShowWindowOption.SW_SHOW.value
                    )
                elif window_placement.showCmd.value == winapi_ShowWindowOption.SW_SHOWMAXIMIZED.value and \
                        (
                            winapi_get_window_long_ptr_w(
                                self.__handle,
                                winapi_GetWindowLongPtrOption.GWL_STYLE.value
                            ).value & winapi_WindowStyle.WS_SYSMENU.value
                        ):
                    winapi_set_window_long_ptr_w(
                        self.__handle,
                        winapi_GetWindowLongPtrOption.GWL_STYLE.value,
                        static_cast(FWCWindows.Style.MAXIMIZED_BORDERLESS.value, winapi_sint32)
                    )

                    winapi_set_window_position(
                        self.__handle,
                        None,
                        0, 0, 0, 0,
                        winapi_SetWindowPositionOption.SWP_FRAMECHANGED.value   |
                        winapi_SetWindowPositionOption.SWP_NOMOVE.value         |
                        winapi_SetWindowPositionOption.SWP_NOSIZE.value
                    )

                    winapi_show_window(
                        self.__handle,
                        winapi_ShowWindowOption.SW_SHOWMAXIMIZED.value
                    )
                return False
            elif message.contents.message.value == winapi_WindowMessage.WM_NCACTIVATE.value:
                result.contents.value = 1
                return False
            elif message.contents.message.value == winapi_WindowMessage.WM_ACTIVATEAPP.value:
                if message.contents.wParam:
                    window_placement: winapi_WINDOWPLACEMENT = winapi_WINDOWPLACEMENT(
                        0, 0, 0,
                        winapi_POINT(0, 0), winapi_POINT(0, 0),
                        winapi_RECT(0, 0, 0, 0),
                        winapi_RECT(0, 0, 0, 0)
                    )

                    winapi_get_window_placement(
                        self.__handle,
                        byref(window_placement)
                    )
                    if window_placement.showCmd.value != winapi_ShowWindowOption.SW_SHOWMINIMIZED.value:
                        winapi_set_window_long_ptr_w(
                            self.__handle,
                            winapi_GetWindowLongPtrOption.GWL_STYLE.value,
                            winapi_get_window_long_ptr_w(
                                self.__handle,
                                winapi_GetWindowLongPtrOption.GWL_STYLE.value
                            ).value & ~ winapi_WindowStyle.WS_CAPTION.value
                        )
                return False
            elif message.contents.message.value == winapi_WindowMessage.WM_ACTIVATE.value:
                pass

