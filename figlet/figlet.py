from pyfiglet import Figlet
import sys
import random

figlet = Figlet() # create an obj of the class before getting "initialized"

###### better put sys.argv in the very first part#####

if len(sys.argv) == 1 or len(sys.argv) == 3:
    match len(sys.argv):
        case 1:
            text = input("Input: ").strip()
            figlet.setFont(font = random.choice(figlet.getFonts())) # but is it good not to give a var?
            print(figlet.renderText(text))
        case 3:
            arg_1 = ["-f", "--font"]
            if sys.argv[1] not in arg_1 or sys.argv[2] not in figlet.getFonts():
                sys.exit("Invalid usage")
            else:
                text = input("Input: ").strip()
                """f = figlet(font = sys.argv[2]) # try first
                print(f.renderText(text))"""
                figlet.setFont(font = sys.argv[2])
                print(figlet.renderText(text))

        case _:# do sth if all cmd-line args are correct
            sys.exit("Invalid usage")

else:
     sys.exit("Invalid usage")

# setFont
# figlet (obj) for another obj (f)?
# def main()