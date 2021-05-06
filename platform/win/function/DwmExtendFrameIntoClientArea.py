import sys

if sys.platform.startswith('win'):
    from ctypes import windll
    from ctypes.wintypes import HWND as winapi_window_handle
    from ..struct.MARGINS import PMARGINS as winapi_MARGINS_pointer
    from ctypes.wintypes import LONG as winapi_sint16

    winapi_result_handle = winapi_sint16
    winapi_desktop_window_manager_result = winapi_result_handle

    DwmExtendFrameIntoClientArea = windll.dwmapi.dwm.DwmExtendFrameIntoClientArea
    DwmExtendFrameIntoClientArea.argtypes = [
        winapi_window_handle,
        winapi_MARGINS_pointer
    ]
    DwmExtendFrameIntoClientArea.restype = winapi_desktop_window_manager_result
