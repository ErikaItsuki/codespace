import sys

# use len with sys.argv which happens to be a list (argv is the funciton)
#    print("hello, my name is" ,sys.argv[1])

def get_name():

    while True:
        if len(sys.argv) > 2:
            print("Too many arguments")
        elif len(sys.argv) < 2:
            print("Too few arguments")
        else:
            return "Hello, my name is " + sys.argv[1]

get_name()




