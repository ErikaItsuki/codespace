from pyfiglet import figlet
import sys
import random

from pyfiglet import Figlet

figlet = Figlet() # create an obj

# sys.argv: python figlet.py -f/--font fontName
text = input("Input: ").strip()
match len(sys.argv):
    case 1:
        f = Figlet(font = random.choice(figlet.getFonts()))
        print(f.renderText(text))
    case 3:
        if sys.argv[1] != "-f" or sys.argv[1] != "--font" or sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")
        else:
            f = figlet.setfont(font = sys.argv[2])
            print(f.renderText(text))

    case _:# do sth if all cmd-line args are correct
        print("sys.argv should have either 1 or 3 items")
