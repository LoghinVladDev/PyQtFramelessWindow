import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import HMONITOR as winapi_monitor_handle
    from ctypes.wintypes import BOOL as winapi_bool
    from ..struct.MONITORINFO import LPMONITORINFO as winapi_MONITORINFO_pointer
    from ctypes import windll

    GetMonitorInfoW = windll.user32.GetMonitorInfoW
    GetMonitorInfoW.argtypes = [
        winapi_monitor_handle,
        winapi_MONITORINFO_pointer
    ]
    GetMonitorInfoW.restype = winapi_bool
