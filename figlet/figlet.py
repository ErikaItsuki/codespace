# prelim

"""
figlet.setFond(font = sys.argv[2])
if sys.argv[2] not in figlet.getFronts()
print(fidlet.renderText(text_u_want_to_print))"""

import random
import sys
import pyfiglet



# purpose of EX
"""
1. train to use multiple libraries (sys, pyfiglet, random)
2.
"""
# Draft

# expecting cmd line args

from pyfiglet import figlet
import sys
import random

from pyfiglet import Figlet

figlet = Figlet() # create an obj

# sys.argv: python figlet.py -f/--font fontName

match len(sys.argv):
    case 1:
        print(figlet.renderText(...))
    case 3:
        if sys.argv[1] != "-f" or sys.argv[1] != "--font" or sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")
    case _:# do sth if all cmd-line args are correct
        ...


# prompts user input str


