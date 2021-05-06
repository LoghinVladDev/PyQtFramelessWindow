import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import HWND as winapi_window_handle
    from ctypes import c_int as c_sint32
    from ctypes.wintypes import UINT as winapi_uint32
    from ctypes.wintypes import BOOL as winapi_bool
    from ctypes import windll

    from enum import Enum


    class SetWindowPosOption(Enum):
        SWP_ASYNCWINDOWPOS  = 0x4000
        SWP_DEFERERASE      = 0x2000
        SWP_DRAWFRAME       = 0x0020
        SWP_FRAMECHANGED    = 0x0020
        SWP_HIDEWINDOW      = 0x0080
        SWP_NOACTIVATE      = 0x0010
        SWP_NOCOPYBITS      = 0x0100
        SWP_NOMOVE          = 0x0002
        SWP_NOOWNERZORDER   = 0x0200
        SWP_NOREDRAW        = 0x0008
        SWP_NOREPOSITION    = 0x0200
        SWP_NOSENDCHANGING  = 0x0400
        SWP_NOSIZE          = 0x0001
        SWP_NOZORDER        = 0x0004
        SWP_SHOWWINDOW      = 0x0040


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
