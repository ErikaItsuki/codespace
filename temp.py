import sys

# sys.exit -> after printing the exit arg, prog exits right away
# generally good to sep the exception handling part and the "print
# name tags"


# multiple arguments:
if len(sys.argv) < 2 :
    sys.exit("Too few arguments")
for arg in sys.argv:
    # print("Hello, my name is ", arg) # will print hello..temp.py
    

