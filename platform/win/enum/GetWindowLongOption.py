import sys

if sys.platform.startswith('win'):
    from enum import Enum

    class GetWindowLongOption(Enum):
        GWL_EXSTYLE         = -20
        GWL_HINSTANCE       = -6
        GWL_ID              = -12
        GWL_STYLE           = -16
        GWL_USERDATA        = -21
        GWL_WNDPROC         = -4

        DWL_MSGRESULT       = 0
        # DWL_DLGPROC       = DWLP_MSGRESULT + sizeof(LRESULT)
        # DWL_USER          = DWLP_DLGPROC + sizeof(DLGPROC)