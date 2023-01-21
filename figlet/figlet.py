from pyfiglet import Figlet
import sys
import random

def main():

    figlet = Figlet()
    print(which_font(figlet))


def which_font(figlet):

    if len(sys.argv) == 1 or len(sys.argv) == 3:
        match len(sys.argv):
            case 1:
                text = input("Input: ").strip()
                figlet.setFont(font = random.choice(figlet.getFonts()))
                return figlet.renderText(text)
            case 3:
                arg_1 = ["-f", "--font"]
                if sys.argv[1] not in arg_1 or sys.argv[2] not in figlet.getFonts():
                    sys.exit("Invalid usage")
                else:
                    text = input("Input: ").strip()
                    """f = figlet(font = sys.argv[2]) # try first
                    print(f.renderText(text))"""
                    figlet.setFont(font = sys.argv[2])
                    return figlet.renderText(text)

            case _:
                sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

        
main()
