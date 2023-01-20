from pyfiglet import Figlet
import sys
import random

figlet = Figlet() # create an obj

###### better put sys.argv in the very first part#####

if len != 1 or 3:
    sys.exit()
else:

    match len(sys.argv):
        case 1:
            text = input("Input: ").strip()
            f = Figlet(font = random.choice(figlet.getFonts()))
            print(f.renderText(text))
        case 3:
            arg_1 = ["-f", "--font"]
            if sys.argv[1] not in arg_1 or sys.argv[2] not in figlet.getFonts():
                sys.exit("Invalid usage")
            else:
                text = input("Input: ").strip()
                f = Figlet(font = sys.argv[2]) # try first
                print(f.renderText(text))

        case _:# do sth if all cmd-line args are correct
            sys.exit("Invalid usage")

# sys.argv: python figlet.py -f/--font fontName

