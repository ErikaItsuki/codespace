from pyfiglet import Figlet
import sys
import random

def main():

    figlet = Figlet() # create an obj of the class before getting "initialized"
    print(which_font(figlet))


def which_font(figlet):
    if len(sys.argv) == 1 or len(sys.argv) == 3:
        match len(sys.argv):
            case 1:
                text = input("Input: ").strip()
                figlet.setFont(font = random.choice(figlet.getFonts())) # but is it good not to give a var?
                                                                        # we already get it stored in the obj so not to return is fine
                                                                        # we use var to store sth that may be lost as the prog progress
                                                                        # but using class takes care of this problem
                                                                        # this process is called instantiating (i.e.) np ~~
                                                                        # setFont is an instance method :D
                # figlet = Figlet.setFont(font = random.choice(figlet.getFonts()))
                # -> TypeError: Figlet.setFont()missing 1 required positional argument: 'self'
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

            case _:# do sth if all cmd-line args are correct
                sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")



main()
# setFont
"""
is a class method : calling syntax = Class_Name.classmethod(...)"""
# figlet (obj) for another obj (f)?
# def main()
