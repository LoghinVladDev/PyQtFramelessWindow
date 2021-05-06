import sys

if sys.platform.startswith('win'):
    from . import DwmExtendFrameIntoClientArea
    from . import GetClientRect
    from . import GetMonitorInfoW
    from . import GetWindowLongPtrW
    from . import GetWindowPlacement
    from . import GetWindowRect
    from . import LoadCursorW
    from . import MonitorFromWindow
    from . import ReleaseCapture
    from . import SendMessage
    from . import SetCursor
    from . import SetWindowLongPtrW
    from . import SetWindowPos
    from . import ShowWindow
