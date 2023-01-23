import sys

counter = 0

if len(sys.argv) == 2:
    # has .gif, .py, .csv
    # if in  these 3: starting from the fullstop, strip away all
    if sys.argv[1].endswith(".py"):
        if sys.argv[1].replace(".py", "") not in  ...:
            raise FileNotFoundError("File does not exist")
        with open("lines.py") as file:
            for line in file:
                if line.lstrip().startswith("#") == False and line.isspace() == False:
                    # strings/char/as a chunk.isspace(): syntax valid
                    counter += 1
        print(counter)
    else:
        raise FileNotFoundError("Not a python file")



elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else: # <2
    sys.exit("Too few command-line arguments")










"""

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

"""