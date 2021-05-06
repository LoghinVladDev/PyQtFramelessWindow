import sys


if sys.platform.startswith('win'):
    from . import GetWindowLongPtrW
    from . import SendMessage
    from . import SetWindowLongPtrW
    from . import ShowWindow
    from . import DwmExtendFrameIntoClientArea
    from . import GetClientRect
    from . import GetWindowRect
    from . import SetWindowPos
