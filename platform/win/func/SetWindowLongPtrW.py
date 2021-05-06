import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import HWND as winapi_window_handle
    from ctypes import c_int as c_sint32
    from ctypes.wintypes import PLONG as winapi_sint32_pointer
    from ctypes import windll

    SetWindowLongPtrW = windll.user32.SetWindowLongPtrW
    SetWindowLongPtrW.argtypes = [
        winapi_window_handle,
        c_sint32,
        winapi_sint32_pointer
    ]
    SetWindowLongPtrW.restype = winapi_sint32_pointer
