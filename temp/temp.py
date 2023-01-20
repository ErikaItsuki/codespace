from pyfiglet import Figlet
import random
import sys

figlet = Figlet() # has attr font = default font

text = input("Input: ").strip()
#print(figlet.renderText(text)) # seems to print default font

if len(sys.argv) == 1:
    f = Figlet(font = random.choice(figlet.getFonts()))
    print(f.renderText(text))
else:
    print("do sth")
