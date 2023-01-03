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
           x = "Hello, my name is " + sys.argv[1] # just like a var but its value
                                                  # is obtained on the command-line
           return x
           
def main():
    print(get_name())

main()







