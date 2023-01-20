from pyfiglet import Figlet

figlet = Figlet() # create an obj

# sys.argv: python figlet.py -f/--font fontName

match len(sys.argv):
    case  1:
        print(figlet.renderText(text))
    case == 3:
        if sys.argv[1] != "-f"
        or sys.argv[1] != "--font"
        or sys.argv[2] not in figlet.getFonts():

        sys.exit("Invalid usage")
    else:# do sth if all cmd-line args are correct
        ...





"""
if len(sys.argv) == 1:
    print(figlet.renderText(text))

elif len(sys.argv) == 3:
    if sys.argv[1] != "-f"
        or sys.argv[1] != "--font"
        or sys.argv[2] not in fidlet.getFont():

        sys.exit("Invalid usage")
    else:# do sth if all cmd-line args are correct
        ...

"""

