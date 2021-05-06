import sys

if sys.platform.startswith('win'):
    from ctypes import Structure
    from ctypes.wintypes import UINT as winapi_uint32
    from ctypes.wintypes import POINT as winapi_POINT
    from ctypes.wintypes import RECT as winapi_RECT
    from ctypes import POINTER as c_pointer


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

    PWINDOWPLACEMENT = c_pointer(WINDOWPLACEMENT)
    LPWINDOWPLACEMENT = c_pointer(WINDOWPLACEMENT)
