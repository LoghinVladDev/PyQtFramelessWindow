import sys

if sys.platform.startswith('win'):
    from . import GetWindowLongOption
    from . import HitTest
    from . import MonitorFromWindowOption
    from . import SetWindowPosOption
    from . import ShowWindowOption
    from . import WindowAnimation
    from . import WindowMessage
    from . import WindowStyle