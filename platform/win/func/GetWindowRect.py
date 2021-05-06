import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import HWND as     winapi_window_handle
    from ctypes.wintypes import LPRECT as   winapi_rect_pointer
    from ctypes.wintypes import BOOL as     winapi_bool
    from ctypes import windll

    GetWindowRect = windll.user32.GetWindowRect
    GetWindowRect.argtypes = [
        winapi_window_handle,
        winapi_rect_pointer
    ]
    GetWindowRect.restype = winapi_bool
