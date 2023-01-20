from pyfiglet import Figlet
import sys
import random

figlet = Figlet() # create an obj

###### better put sys.argv in the very first part#####
match len(sys.argv):
    case 1:
        text = input("Input: ").strip()
        f = Figlet(font = random.choice(figlet.getFonts()))
        print(f.renderText(text))
    case 3:
        text = input("Input: ").strip()
        arg_1 = ["-f", "--font"]
        if sys.argv[1] not in arg_1 or sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")
        else:
            f = Figlet(font = sys.argv[2]) # try first
            print(f.renderText(text))

    case _:# do sth if all cmd-line args are correct
        sys.exit("Invalid usage")

# sys.argv: python figlet.py -f/--font fontName