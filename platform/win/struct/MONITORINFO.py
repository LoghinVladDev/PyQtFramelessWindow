import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import DWORD as winapi_dword_uint32
    from ctypes.wintypes import RECT as winapi_RECT
    from ctypes import POINTER as c_pointer
    from ctypes import Structure


    class MONITORINFO(Structure):
        _fields_ = [
            ('cbSize', winapi_dword_uint32),
            ('rcMonitor', winapi_RECT),
            ('rcWork', winapi_RECT),
            ('dwFlags', winapi_dword_uint32)
        ]

    PMONITORINFO = c_pointer(MONITORINFO)
    LPMONITORINFO = c_pointer(MONITORINFO)
