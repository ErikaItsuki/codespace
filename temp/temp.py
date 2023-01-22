import sys

try:
    # check if exactly 1 CLA:
    if len(sys.argv) > 1:
        sys.exit("Too many command-line arguments")
    #else:
    #    sys.exit("")
    elif len(sys.argv) < 1:
        sys.exit("Too few command-line arguments")
    elif sys.argv[0].endswith(".py") :
        print("it's good")
    else:
        print("not yet done")

except FileNotFoundError: # no use too XD
    print("Not a Python file")


    #print("Not a Python file") # no use on Errno2
    """sys.argv
    with open("")"""


# if python names.py: with open("names.txt", "r") as file:
# for line in file:
# global counter++ (init = 0)
# out of with: print counter
