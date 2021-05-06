import sys

if sys.platform.startswith('win'):
    from enum import Enum


    class HitTest(Enum):
        HTERROR         = -2
        HTTRANSPARENT   = -1
        HTNOWHERE       = 0
        HTCLIENT        = 1
        HTCAPTION       = 2
        HTSYSMENU       = 3
        HTGROWBOX       = 4
        HTSIZE          = HTGROWBOX.value
        HTMENU          = 5
        HTHSCROLL       = 6
        HTVSCROLL       = 7
        HTMINBUTTON     = 8
        HTMAXBUTTON     = 9
        HTLEFT          = 10
        HTRIGHT         = 11
        HTTOP           = 12
        HTTOPLEFT       = 13
        HTTOPRIGHT      = 14
        HTBOTTOM        = 15
        HTBOTTOMLEFT    = 16
        HTBOTTOMRIGHT   = 17
        HTBORDER        = 18
        HTREDUCE        = HTMINBUTTON.value
        HTZOOM          = HTMAXBUTTON.value
        HTSIZEFIRST     = HTLEFT.value
        HTSIZELAST      = HTBOTTOMRIGHT.value
        HTOBJECT        = 19
        HTCLOSE         = 20
        HTHELP          = 21