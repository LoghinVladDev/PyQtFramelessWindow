import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import HWND as winapi_window_handle
    from ctypes import c_int as c_sint32
    from ctypes.wintypes import UINT as winapi_uint32
    from ctypes.wintypes import BOOL as winapi_bool
    from ctypes import windll

    SetWindowPos = windll.user32.SetWindowPos
    SetWindowPos.argtypes = [
        winapi_window_handle,
        winapi_window_handle,
        c_sint32,
        c_sint32,
        c_sint32,
        c_sint32,
        winapi_uint32
    ]
    SetWindowPos.restype = winapi_bool
