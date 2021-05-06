import sys

if sys.platform.startswith('win'):
    from ctypes import Structure
    from ctypes import c_int as c_sint32
    from ctypes import POINTER as c_pointer

    class MARGINS(Structure):
        _fields_ = [
            ('cxLeftWidth', c_sint32),
            ('cxRightWidth', c_sint32),
            ('cyTopHeight', c_sint32),
            ('cyBottomHeight', c_sint32)
        ]

    PMARGINS = c_pointer(MARGINS)
    LPMARGINS = c_pointer(MARGINS)
