from pyfiglet import Figlet

figlet = Figlet() # create an obj

figlet.setFont(font = "5lineoblique")

# sys.argv: python figlet.py -f/--font fontName

if sys.argv[1] != "-f" or sys.argv[1] != "--font" or sys.argv[2] != 


