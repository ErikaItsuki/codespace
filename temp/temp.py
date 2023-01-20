from pyfiglet import Figlet
import sys
import random

figlet = Figlet() # create an obj

###### better put sys.argv in the very first part#####
arg_1 = ["-f", "--font"]

if sys.argv[1] not in arg_1 or sys.argv[2] not in figlet.getFonts():
    sys.exit("Invalid usage")
    
else:
    text = input("Input: ").strip()

    match len(sys.argv):
        case 1:
            f = Figlet(font = random.choice(figlet.getFonts()))
            print(f.renderText(text))
        case 3:

            if sys.argv[1] not in arg_1 or sys.argv[2] not in figlet.getFonts():
                sys.exit("Invalid usage")
            else:
                f = Figlet(font = sys.argv[2]) # try first
                print(f.renderText(text))

        case _:# do sth if all cmd-line args are correct
            sys.exit("Invalid usage")







# sys.argv: python figlet.py -f/--font fontName