import sys

if sys.platform.startswith('win'):
    from enum import Enum

    class WindowAnimation(Enum):
        WA_INACTIVE     = 0
        WA_ACTIVE       = 1
        WA_CLICKACTIVE  = 2
