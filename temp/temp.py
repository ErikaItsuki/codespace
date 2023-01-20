from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

text = input("Input: ").strip()
print(figlet.renderText(text))

