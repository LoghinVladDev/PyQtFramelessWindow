import sys

if sys.platform.startswith('win'):
    from . import enum
    from . import function
    from . import struct
