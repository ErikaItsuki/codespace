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


len == 1:
1. endswith.py