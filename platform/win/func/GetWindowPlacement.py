import sys


if sys.platform.startswith('wim'):
    from ctypes.wintypes import HWND as winapi_window_handle
    from ctypes import POINTER as c_pointer
    from ctypes import Structure
    from ctypes.wintypes import UINT as winapi_uint32
    from ctypes.wintypes import POINT as winapi_POINT
    from ctypes.wintypes import RECT as winapi_RECT
    from ctypes.wintypes import BOOL as winapi_bool
    from ctypes import windll


    class WINDOWPLACEMENT(Structure):
        _fields_ = [
            ('length', winapi_uint32),
            ('flags', winapi_uint32),
            ('showCmd', winapi_uint32),
            ('ptMinPosition', winapi_POINT),
            ('ptMaxPosition', winapi_POINT),
            ('rcNormalPosition', winapi_RECT),
            ('rcDevice', winapi_RECT)
        ]

    GetWindowPlacement = windll.user32.GetWindowPlacement
    GetWindowPlacement.argtypes = [
        winapi_window_handle,
        c_pointer(WINDOWPLACEMENT)
    ]
    GetWindowPlacement.restype = winapi_bool
