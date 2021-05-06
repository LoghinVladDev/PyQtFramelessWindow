import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import HICON as HCURSOR
    from ctypes import windll

    winapi_cursor_handle = HCURSOR

    SetCursor = windll.user32.SetCursor
    SetCursor.argtypes = [
        winapi_cursor_handle
    ]
    SetCursor.restype = winapi_cursor_handle
