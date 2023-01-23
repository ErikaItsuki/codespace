
"""  a correct draft
len == 1:
1. endswith.py
2. endswith not .py

len > 1
1. [0].py, [1]or... not with .py -> not a py file
2. [0].py, [1]DNE -> file NDE
3. [0].py, [1]have no .py/txt... -> too many"""


import sys

counter = 0

try:
    if len(sys.argv) == 2:

        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1]) as file: # raise filenotfounderror with except
                for line in file:
                    if line.lstrip().startswith("#") == False and line.isspace() == False:
                        counter += 1
            print(counter)
        else:
            sys.exit("Not a python file")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    else: # <2
        sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")
