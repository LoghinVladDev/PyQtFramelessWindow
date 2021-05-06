import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import HMONITOR as winapi_monitor_handle
    from ctypes.wintypes import HWND as winapi_window_handle
    from ctypes.wintypes import DWORD as winapi_dword_uint32
    from ctypes import windll

    MonitorFromWindow = windll.user32.MonitorFromWindow
    MonitorFromWindow.argtypes = [
        winapi_window_handle,
        winapi_dword_uint32
    ]
    MonitorFromWindow.restype = winapi_monitor_handle
