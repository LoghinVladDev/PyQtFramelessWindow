import sys

if sys.platform.startswith('win'):
    from enum import Enum


    class ShowWindowOption(Enum):
        SW_HIDE = 0
        SW_SHOWNORMAL = 1
        SW_NORMAL = SW_SHOWNORMAL.value
        SW_SHOWMINIMIZED = 2
        SW_SHOWMAXIMIZED = 3
        SW_MAXIMIZE = SW_SHOWMAXIMIZED.value
        SW_SHOWNOACTIVATE = 4
        SW_SHOW = 5
        SW_MINIMIZE = 6
        SW_SHOWMINNOACTIVE = 7
        SW_SHOWNA = 8
        SW_RESTORE = 9
        SW_SHOWDEFAULT = 10
        SW_FORCEMINIMIZE = 11