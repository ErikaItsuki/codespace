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




