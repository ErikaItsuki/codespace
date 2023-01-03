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
            return print("Hello, my name is " + sys.argv[1])
            # valid but not very good
            # better = def main(): print(get_name), than call main()
            # OR simply print inside else, and break

get_name()





