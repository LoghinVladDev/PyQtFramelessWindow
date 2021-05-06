import sys


if sys.platform.startswith('win'):
    from . import WindowMessage
    from . import WindowStyle
    from . import func
