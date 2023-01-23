import sys

counter = 0

# check if exactly 1 CLA:
if len(sys.argv) > 1: # ass one more: if sys.argv.replace(".py", "") != "lines" -> File does not exist
    sys.exit("Too many command-line arguments")
#else:
#    sys.exit("")
elif len(sys.argv) < 1:
    sys.exit("Too few command-line arguments")
elif sys.argv[0] == "lines.py" :
    with open("lines.py") as file:
        for line in file:
            """# line.lstrip() # why cant i strip ?
            if line.startswith("#") == False:
                # check if the i-1 line ends with "\n"
                counter += 1
            else:
                pass"""
            if line.lstrip().startswith("#") == False and line.isspace() == False:
                # strings/char/as a chunk.isspace(): syntax valid
                counter += 1

    print(counter)
else:
    raise FileNotFoundError("Not a Python file") # no use too XD, neither OSError nor FileNotFoundError