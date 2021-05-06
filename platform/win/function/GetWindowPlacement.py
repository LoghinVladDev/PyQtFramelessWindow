import sys

if sys.platform.startswith('wim'):
    from ctypes.wintypes import HWND as winapi_window_handle
    from ctypes.wintypes import BOOL as winapi_bool
    from ctypes import windll

    from ..struct.WINDOWPLACEMENT import LPWINDOWPLACEMENT as winapi_WINDOWPLACEMENT_pointer

    GetWindowPlacement = windll.user32.GetWindowPlacement
    GetWindowPlacement.argtypes = [
        winapi_window_handle,
        winapi_WINDOWPLACEMENT_pointer
    ]
    GetWindowPlacement.restype = winapi_bool
