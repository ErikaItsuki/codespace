from pyfiglet import Figlet

figlet = Figlet() # create an obj

figlet.setFont(font = "5lineoblique")

# sys.argv: python figlet.py -f/--font fontName

if sys.argv[1] != "-f" or sys.argv[1] != "--font" :
    sys.exit("unrecognized command")
elif sys.argv[2] != ...(getting the Name of font of all):
    sys.exit("sorry, no such font")
else: # do sth if all cmd-line args are correct
    ...


