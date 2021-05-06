import sys

if sys.platform.startswith('win'):
    from enum import Enum

    import fwc
    import fwc_types

    from ctypes import c_void_p as          c_void_pointer
    from ctypes import c_long as            c_sint32
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
    from ctypes.wintypes import DWORD as    winapi_dword_uint32
    from ctypes.wintypes import PULONG as   winapi_uint32_pointer
    from ctypes.wintypes import PLONG as    winapi_sint32_pointer
    from ctypes.wintypes import RECT as     winapi_RECT
    from ctypes.wintypes import LONG as     winapi_sint32

    from ctypes.wintypes import MSG as      winapi_MSG

    from ctypes.wintypes import POINT as    winapi_POINT

    from ctypes.wintypes import HMONITOR as winapi_monitor_handle

    from ctypes import sizeof as c_sizeof

    winapi_lresult = winapi_sint32_pointer

    from ctypes import byref

    from ..platform.win.enum.GetWindowLongOption import GetWindowLongOption as                          winapi_GetWindowLongPtrOption
    from ..platform.win.enum.WindowMessage import WindowMessage as                                      winapi_WindowMessage
    from ..platform.win.enum.ShowWindowOption import ShowWindowOption as                                winapi_ShowWindowOption
    from ..platform.win.enum.WindowStyle import WindowStyle as                                          winapi_WindowStyle
    from ..platform.win.enum.SetWindowPosOption import SetWindowPosOption as                            winapi_SetWindowPositionOption
    from ..platform.win.enum.WindowAnimation import WindowAnimation as                                  winapi_WindowAnimation
    from ..platform.win.enum.HitTest import HitTest as                                                  winapi_HitTest
    from ..platform.win.enum.MonitorFromWindowOption import MonitorFromWindowOption as                  winapi_MonitorFromWindowOption

    from ..platform.win.struct.MARGINS import MARGINS as                                                winapi_MARGINS
    from ..platform.win.struct.WINDOWPLACEMENT import WINDOWPLACEMENT as                                winapi_WINDOWPLACEMENT
    from ..platform.win.struct.MINMAXINFO import MINMAXINFO as                                          winapi_MINMAXINFO
    from ..platform.win.struct.MINMAXINFO import LPMINMAXINFO as                                        winapi_MINMAXINFO_pointer
    from ..platform.win.struct.MONITORINFO import MONITORINFO as                                        winapi_MONITORINFO

    from ..platform.win.function.GetWindowLongPtrW import GetWindowLongPtrW as                          winapi_get_window_long_ptr_w
    from ..platform.win.function.SetWindowLongPtrW import SetWindowLongPtrW as                          winapi_set_window_long_ptr_w
    from ..platform.win.function.ShowWindow import ShowWindow as                                        winapi_show_window
    from ..platform.win.function.SendMessage import SendMessage as                                      winapi_send_message
    from ..platform.win.function.DwmExtendFrameIntoClientArea import DwmExtendFrameIntoClientArea as    winapi_dwm_extend_frame_into_client_area
    from ..platform.win.function.SetWindowPos import SetWindowPos as                                    winapi_set_window_position
    from ..platform.win.function.GetClientRect import GetClientRect as                                  winapi_get_client_rect
    from ..platform.win.function.GetWindowRect import GetWindowRect as                                  winapi_get_window_rect
    from ..platform.win.function.GetWindowPlacement import GetWindowPlacement as                        winapi_get_window_placement
    from ..platform.win.function.ReleaseCapture import ReleaseCapture as                                winapi_release_capture
    from ..platform.win.function.LoadCursorW import LoadCursorW as                                      winapi_load_cursor_w
    from ..platform.win.function.SetCursor import SetCursor as                                          winapi_set_cursor
    from ..platform.win.function.MonitorFromWindow import MonitorFromWindow as                          winapi_monitor_from_window
    from ..platform.win.function.GetMonitorInfoW import GetMonitorInfoW as                              winapi_get_monitor_info_w


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

        def set_frameless(self, enabled: bool) -> None:
            new_style: FWCWindows.Style = FWCWindows.Style.AERO_BORDERLESS if enabled else FWCWindows.Style.WINDOWED
            old_style: FWCWindows.Style

            old_style_casted: c_uint64 = static_cast(winapi_get_window_long_ptr_w(
                self.__handle,
                winapi_GetWindowLongPtrOption.GWL_STYLE.value
            ), c_uint64)

            if old_style_casted.value == FWCWindows.Style.WINDOWED.value:
                old_style = FWCWindows.Style.WINDOWED
            elif old_style_casted.value == FWCWindows.Style.AERO_BORDERLESS.value:
                old_style = FWCWindows.Style.AERO_BORDERLESS
            else:
                old_style = FWCWindows.Style.MAXIMIZED_BORDERLESS

            if new_style != old_style:
                winapi_set_window_long_ptr_w(
                    self.__handle,
                    winapi_GetWindowLongPtrOption.GWL_STYLE.value,
                    winapi_sint32(new_style.value)
                )

                self.set_enable_shadow()

                winapi_set_window_position(
                    self.__handle, None,
                    0, 0, 0, 0,
                    winapi_SetWindowPositionOption.SWP_FRAMECHANGED.value   |
                    winapi_SetWindowPositionOption.SWP_NOMOVE.value         |
                    winapi_SetWindowPositionOption.SWP_NOSIZE.value
                )

                winapi_show_window(
                    self.__handle,
                    winapi_ShowWindowOption.SW_SHOW.value
                )

        def convert_to_frameless(self) -> None:
            self.__handle: winapi_window_handle = static_cast(super().q.window_handle, winapi_window_handle)
            self.set_frameless(True)

        def convert_to_window_with_frame(self) -> None:
            self.set_frameless(False)

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
            casted_message: c_pointer(winapi_MSG) = static_cast(message, c_pointer(winapi_MSG))

            if casted_message.contents.message.value == winapi_WindowMessage.WM_NCCALCSIZE.value:
                if casted_message.contents.wParam.value:
                    result.contents.value = 0
                    return True
            elif casted_message.contents.message.value == winapi_WindowMessage.WM_WINDOWPOSCHANGING.value:
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
            elif casted_message.contents.message.value == winapi_WindowMessage.WM_NCACTIVATE.value:
                result.contents.value = 1
                return False
            elif casted_message.contents.message.value == winapi_WindowMessage.WM_ACTIVATEAPP.value:
                if casted_message.contents.wParam.value:
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
            elif casted_message.contents.message.value == winapi_WindowMessage.WM_ACTIVATE.value:
                if u_long_low(casted_message.contents.wParam.value).value == winapi_WindowAnimation.WA_ACTIVE.value and \
                        u_long_high(casted_message.contents.wParam.value).value == 0:
                    winapi_set_window_long_ptr_w(
                        self.__handle,
                        winapi_GetWindowLongPtrOption.GWL_STYLE.value,
                        winapi_get_window_long_ptr_w(
                            self.__handle,
                            winapi_GetWindowLongPtrOption.GWL_STYLE.value
                        ).value & ~ winapi_WindowStyle.WS_CAPTION.value
                    )
                elif u_long_low(casted_message.contents.wParam.value).value == winapi_WindowAnimation.WA_INACTIVE.value and \
                        u_long_high(casted_message.contents.wParam.value).value == 0:
                    winapi_set_window_long_ptr_w(
                        self.__handle,
                        winapi_GetWindowLongPtrOption.GWL_STYLE.value,
                        winapi_get_window_long_ptr_w(
                            self.__handle,
                            winapi_GetWindowLongPtrOption.GWL_STYLE.value
                        ).value | winapi_WindowStyle.WS_CAPTION.value
                    )
                return False
            elif casted_message.contents.message.value == winapi_WindowMessage.WM_NCHITTEST.value:
                return False
            elif casted_message.contents.message.value == winapi_WindowMessage.WM_LBUTTONDBLCLK.value:
                mouse_pos: fwc_types.FWCPoint.FWCPoint = fwc_types.FWCPoint.FWCPoint(self.get_current_mouse_pos(casted_message.contents.lParam))

                if not super().q.should_perform_window_drag(mouse_pos.x, mouse_pos.y):
                    return False

                if super().do_border_hit_test(
                    self.get_current_client_rect(),
                    mouse_pos,
                    super().q.border_width() == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.CLIENT.value
                ):
                    winapi_release_capture()
                    winapi_send_message(
                        self.__handle,
                        winapi_WindowMessage.WM_NCLBUTTONDBLCLK.value,
                        winapi_HitTest.HTCAPTION.value,
                        casted_message.contents.lParam.value
                    )

                return False
            elif casted_message.contents.message.value == winapi_WindowMessage.WM_LBUTTONDOWN.value:
                mouse_pos: fwc_types.FWCPoint.FWCPoint = self.get_current_mouse_pos(casted_message.contents.lParam)
                hit_result: fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult

                if super().q.enable_resizing:
                    hit_result = super().do_border_hit_test(
                        self.get_current_client_rect(),
                        mouse_pos,
                        super().q.border_width
                    )
                else:
                    hit_result = super().do_border_hit_test(
                        self.get_current_client_rect(),
                        mouse_pos,
                        0
                    )

                hit_location: winapi_HitTest
                if hit_result.value == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.LEFT:
                    hit_location = winapi_HitTest.HTLEFT
                elif hit_result.value == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.RIGHT:
                    hit_location = winapi_HitTest.HTRIGHT
                elif hit_result.value == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.TOP:
                    hit_location = winapi_HitTest.HTTOP
                elif hit_result.value == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.BOTTOM:
                    hit_location = winapi_HitTest.HTBOTTOM
                elif hit_result.value == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.BOTTOM_LEFT:
                    hit_location = winapi_HitTest.HTBOTTOMLEFT
                elif hit_result.value == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.BOTTOM_RIGHT:
                    hit_location = winapi_HitTest.HTBOTTOMRIGHT
                elif hit_result.value == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.TOP_LEFT:
                    hit_location = winapi_HitTest.HTTOPLEFT
                elif hit_result.value == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.TOP_RIGHT:
                    hit_location = winapi_HitTest.HTTOPRIGHT
                else:
                    if super().q.should_perform_window_drag(mouse_pos.x, mouse_pos.y):
                        winapi_release_capture()
                        winapi_send_message(
                            self.__handle,
                            winapi_WindowMessage.WM_NCLBUTTONDOWN.value,
                            winapi_HitTest.HTCAPTION.value,
                            casted_message.contents.lParam.value
                        )

                    return False

                winapi_release_capture()
                winapi_send_message(
                    self.__handle,
                    winapi_WindowMessage.WM_NCLBUTTONDOWN.value,
                    hit_location.value,
                    casted_message.contents.lParam.value
                )

                return False
            elif casted_message.contents.message.value == winapi_WindowMessage.WM_MOUSEMOVE.value:
                if not super().q.enable_resizing:
                    return False

                hit_result: fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult = super().do_border_hit_test(
                    self.get_current_client_rect(),
                    self.get_current_mouse_pos(casted_message.contents.lParam),
                    super().q.border_width
                )

                cursor_name: CursorNames

                if hit_result == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.LEFT:
                    cursor_name = CursorNames.WEST_EAST
                elif hit_result == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.RIGHT:
                    cursor_name = CursorNames.WEST_EAST
                elif hit_result == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.TOP:
                    cursor_name = CursorNames.NORTH_SOUTH
                elif hit_result == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.BOTTOM:
                    cursor_name = CursorNames.NORTH_SOUTH
                elif hit_result == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.BOTTOM_LEFT:
                    cursor_name = CursorNames.NORTH_EAST_SOUTH_WEST
                elif hit_result == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.BOTTOM_RIGHT:
                    cursor_name = CursorNames.NORTH_WEST_SOUTH_EAST
                elif hit_result == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.TOP_LEFT:
                    cursor_name = CursorNames.NORTH_WEST_SOUTH_EAST
                elif hit_result == fwc_types.FWCBorderHitTestResult.FWCBorderHitTestResult.TOP_RIGHT:
                    cursor_name = CursorNames.NORTH_EAST_SOUTH_WEST
                else:
                    cursor_name = CursorNames.ARROW

                winapi_set_cursor(winapi_load_cursor_w(None, get_cursor_resource(cursor_name)))

                return False

            elif casted_message.contents.message.value == winapi_WindowMessage.WM_GETMINMAXINFO.value:
                min_max_info: winapi_MINMAXINFO_pointer = static_cast(casted_message.contents.lParam, winapi_MINMAXINFO_pointer)
                monitor_handle: winapi_monitor_handle = winapi_monitor_from_window(
                    self.__handle,
                    winapi_MonitorFromWindowOption.MONITOR_DEFAULTTONEAREST.value
                )
                monitor_info: winapi_MONITORINFO = winapi_MONITORINFO(
                    0,
                    winapi_RECT(0, 0, 0, 0),
                    winapi_RECT(0, 0, 0, 0),
                    0
                )
                monitor_info.cbSize = c_sizeof(winapi_MONITORINFO)
                winapi_get_monitor_info_w(monitor_handle, byref(monitor_info))

                min_max_info.ptMaxPosition.x = 0
                min_max_info.ptMaxPosition.y = 0

                if super().fullscreen:
                    min_max_info.ptMaxSize.x = monitor_info.rcMonitor.right - monitor_info.rcMonitor.left
                    min_max_info.ptMaxSize.y = monitor_info.rcMonitor.bottom - monitor_info.rcMonitor.top
                else:
                    min_max_info.ptMaxSize.x = monitor_info.rcWork.right - monitor_info.rcWork.left
                    min_max_info.ptMaxSize.y = monitor_info.rcWork.bottom - monitor_info.rcWork.top

                min_max_info_used: bool = False
                if super().q.minimum_window_width >= 0:
                    min_max_info.ptMinTrackSize.x = super().q.minimum_window_width
                    min_max_info_used = True
                if super().minimum_window_height >= 0:
                    min_max_info.ptMinTrackSize.y = super().q.minimum_window_height
                    min_max_info_used = True
                if super().maximum_window_width >= 0:
                    min_max_info.ptMaxTrackSize.x = super().q.maximum_window_width
                    min_max_info_used = True
                if super().maximum_window_height >= 0:
                    min_max_info.ptMaxTrackSize.y = super().q.maximum_window_height
                    min_max_info_used = True

                if min_max_info_used:
                    result.contents = 0
                    return True

                return False
            return False