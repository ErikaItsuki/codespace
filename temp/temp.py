import sys

for i in range(len(sys.argv)): # len(sys.argv) returns an object that is not iterable
                               # add range() to fix
    print("Hello", sys.argv[i])