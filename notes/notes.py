"""
Redo to learn more:
P6 Q1: not too many if-else

"""




# Pset6 Q1

"""EXCEPT the Q sys.argv[1] was misunderstood, the idea is ok"""

import sys
counter = 0
# check if exactly 1 CLA:
if len(sys.argv) > 1: # ass one more: if sys.argv.replace(".py", "") != "lines" -> File does not exist
    sys.exit("Too many command-line arguments")
#else:
#    sys.exit("")



if sys.argv[0] == "lines.py" :
    if len(sys.argv) == 1:
        with open("lines.py") as file:
            for line in file:
                if line.lstrip().startswith("#") == False and line.isspace() == False:
                    # strings/char/as a chunk.isspace(): syntax valid
                    counter += 1
        print(counter)
    elif sys.argv[0].endswith(".py") == True:
        raise("File does not exitst")
    elif len(sys.argv) < 1:
        sys.exit("Too few command-line arguments")


else:
    raise FileNotFoundError("Not a Python file") # no use too XD, neither OSError nor FileNotFoundError


# final sol

### better check discord before submission ###


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
                        # strings/char/as a chunk.isspace(): syntax valid
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


#########################_Questions_#####################################
#  (Pset6 Q2) why can't simply do import tabulate, but from ...         #
#                                                                       #
#########################################################################

# trying out tabulate for Pset6, Q2
from tabulate import tabulate # must have from...

# all optional args as default:
table = [["apple", 1], ["orange,", 2]]
dictionary = {"name" : ["A", "B"], "number" : ["1","2"]}

print(tabulate(table))
print(tabulate(dictionary))

print("#################")

# headers
print(tabulate(table, headers = ["items", "number"]))
print(tabulate(dictionary, headers = "firstrow"))
print(tabulate(dictionary, headers = "keys"))

print("#################")

"""
headers=["Planet","R (km)", "mass (x 10^29 kg)"]))
headers="firstrow"
headers="keys"
"""


# row indices
"""showindex="always" or showindex=True"""

# table format
print(tabulate(dictionary, headers = ["name", "number"], tablefmt = "pretty"))
# -> look at pypi.org for all the tablefmt available

### execute to look at the outputs ###

#Pset6 Q2 answer

# what is wget?

import sys
import csv
from tabulate import tabulate # tabulate(table), where table = [[], [], []...]

try:
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
             with open(sys.argv[1]) as file: # file is now a var to sys.argv[1]
                # reader = csv.reader(sys.argv[1]) # no! It prints out regular.csv all letters vertically
                # for line in reader: # here line is a list
                """reader = csv.reader(file)
                print(tabulate(reader, headers = "firstrow", tablefmt = "grid"))"""
                dictreader = csv.DictReader(file)
                # print(dictreader) # no __str__ ????? : it gives a memory address
                print(tabulate(dictreader, headers = "keys", tablefmt = "grid")) # keys are Regular Pizza, Small, and Large
                """
                #print(tabulate(dictreader, headers = "firstrow", tablefmt = "grid")) # firstrows = Cheese, 13.50, 18.95
                # I guess this is because keys are not counted as a row , so the original second row becomes the first, the
                # keys are gone (not printed)
                # csv.DictReader() seems to turn the first row to keys-> but better relearn everytime you use it"""

        else:
            sys.exit("Not a CSV file")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    else:
        sys.exit("Too few command-line arguments")

except FileNotFoundError:
    sys.exit("File does not exist")

# left to do:
# try raise FileNotFoundError (recommended)