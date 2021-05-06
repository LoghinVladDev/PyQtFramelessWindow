import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import POINT as winapi_POINT
    from ctypes import POINTER as c_pointer
    from ctypes import Structure

    class MINMAXINFO(Structure):
        _fields_ = [
            ('ptReserved', winapi_POINT),
            ('ptMaxSize', winapi_POINT),
            ('ptMaxPosition', winapi_POINT),
            ('ptMinTrackSize', winapi_POINT),
            ('ptMaxTrackSize', winapi_POINT)
        ]

    PMINMAXINFO = c_pointer(MINMAXINFO)
    LPMINMAXINFO = c_pointer(MINMAXINFO)
