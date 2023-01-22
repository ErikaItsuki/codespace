import sys

counter = 0

try:
    # check if exactly 1 CLA:
    if len(sys.argv) > 1:
        sys.exit("Too many command-line arguments")
    #else:
    #    sys.exit("")
    elif len(sys.argv) < 1:
        sys.exit("Too few command-line arguments")
    elif sys.argv[0].endswith(".py") :
        file_name = str(sys.argv[0]).replace('.py', '.txt')
        with open(file_name) as file:
            for line in file:
                if line.rstrip().startswith("#") == False:
                 # check if the i-1 line ends with "\n"
                    counter += 1
                else:
                    pass
        print(counter)
    else:
        raise FileNotFoundError("Not a Python file")

except OSError: # no use too XD, neither OSError nor FileNotFoundError
    print("Not a Python file")


    #print("Not a Python file") # no use on Errno2
    """sys.argv
    with open("")"""


# if python names.py: with open("names.txt", "r") as file:
# for line in file:
# global counter++ (init = 0)
# out of with: print counter
