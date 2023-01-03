import sys

# sys.exit -> after printing the exit arg, prog exits right away
# generally good to sep the exception handling part and the "print
# name tags"

if len(sys.argv) < 2 :
    sys.exit("Too few arguments")
elif len(sys.argv) > 2 :
    sys.exit("Too many arguments")

print("Hello, my name is ", sys.argv[1])