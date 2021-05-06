import sys

if sys.platform.startswith('win'):
    from ctypes.wintypes import BOOL as winapi_bool
    from ctypes import windll

    ReleaseCapture = windll.user32.ReleaseCapture
    ReleaseCapture.argtypes = []
    ReleaseCapture.restype = winapi_bool