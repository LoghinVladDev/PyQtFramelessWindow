import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import HWND as winapi_window_handle
    from ctypes import c_int as c_sint32
    from ctypes.wintypes import BOOL as winapi_bool
    from ctypes import windll

    ShowWindow = windll.user32.ShowWindow
    ShowWindow.argtypes = [
        winapi_window_handle,
        c_sint32
    ]
    ShowWindow.restype = winapi_bool
