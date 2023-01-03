def hypotenuse(x, y):
    return x ** 2 + y ** 2 # syntax = number ** expo
    # retrun x*x + y*y
    # return pow(x, 2) + pow(y, 2) # syntax of pow()
                                 # = pow(base, expo, (modulo: result of first 2 args then % by the third args))
    #return math.pow(base, expo) # only takes 2 args, and always returns a float
def main():
    x = int(input("What's x? "))
    y = int(input("What's y? "))
    print("The Hypotenuse is ",hypotenuse(x, y))

main()
# float x, and y -> float z
# calculate z (use pyth.thm)

