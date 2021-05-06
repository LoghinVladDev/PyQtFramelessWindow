import sys

if sys.platform.startswith('win'):
    from . import MARGINS
    from . import MINMAXINFO
    from . import MONITORINFO
    from . import WINDOWPLACEMENT
