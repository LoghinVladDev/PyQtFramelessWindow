import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import HWND as     winapi_window_handle
    from ctypes import c_int as             c_sint32
    from ctypes.wintypes import PLONG as    winapi_sint32_pointer
    from ctypes import windll

    from enum import Enum


    class GetWindowLongOption(Enum):
        GWL_EXSTYLE         = -20
        GWL_HINSTANCE       = -6
        GWL_ID              = -12
        GWL_STYLE           = -16
        GWL_USERDATA        = -21
        GWL_WNDPROC         = -4

        DWL_MSGRESULT       = 0
        # DWL_DLGPROC       = DWLP_MSGRESULT + sizeof(LRESULT)
        # DWL_USER          = DWLP_DLGPROC + sizeof(DLGPROC)

    GetWindowLongPtrW = windll.user32.GetWindowLongPtrW
    GetWindowLongPtrW.argtypes = [
        winapi_window_handle,
        c_sint32
    ]
    GetWindowLongPtrW.restype = winapi_sint32_pointer
