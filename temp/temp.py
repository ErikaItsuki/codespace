from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

text = input("Input: ").strip()
#print(figlet.renderText(text)) # seems to print default font

if len(sys.argv) == 1:
     = figlet.renderText(text)
print(random.choice(figlet.getFonts()))
