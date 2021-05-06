import sys

if sys.platform.startswith('win'):
    from enum import Enum


    class MonitorFromWindowOption(Enum):
        MONITOR_DEFAULTTONULL       = 0x00000000
        MONITOR_DEFAULTTOPRIMARY    = 0x00000001
        MONITOR_DEFAULTTONEAREST    = 0x00000002
