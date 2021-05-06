import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import HWND as winapi_window_handle
    from ctypes import c_uint as c_uint32
    from ctypes.wintypes import WPARAM as winapi_wparam
    from ctypes.wintypes import LPARAM as winapi_lparam
    from ctypes.wintypes import PLONG as winapi_lresult
    from ctypes import windll

    SendMessage = windll.user32.SendMessage
    SendMessage.argtypes = [
        winapi_window_handle,
        c_uint32,
        winapi_wparam,
        winapi_lparam
    ]
    SendMessage.restype = winapi_lresult
