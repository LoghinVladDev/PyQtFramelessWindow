import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import HINSTANCE as winapi_instance_handle
    from ctypes.wintypes import LPCWSTR as winapi_wchar_const_pointer
    from ctypes.wintypes import HICON as HCURSOR
    from ctypes import windll

    winapi_cursor_handle = HCURSOR

    LoadCursorW = windll.user32.LoadCursorW
    LoadCursorW.argtypes = [
        winapi_instance_handle,
        winapi_wchar_const_pointer
    ]
    LoadCursorW.restype = winapi_cursor_handle
