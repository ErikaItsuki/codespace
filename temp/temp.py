from pyfiglet import Figlet
import sys
import random

figlet = Figlet() # create an obj


text = input("Input: ").strip()
match len(sys.argv):
    case 1:
        f = Figlet.setFont(font = random.choice(figlet.getFonts()))
        print(f.renderText(text))
    case 3:
        arg_1 = ["-f", "--font"]
        if sys.argv[1] not in arg_1 or sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")
        else:
            f = figlet.setFont(font = sys.argv[2])
            print(f.renderText(text))

    case _:# do sth if all cmd-line args are correct
        print("sys.argv should have either 1 or 3 items")

# sys.argv: python figlet.py -f/--font fontName