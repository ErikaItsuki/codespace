def median(x, y, z):
    # think about it: how many cases of results? How many conditions for each result?
    if y < x < z or z < x < y:
        return x
    if z < y < x or x < y < z:
        return y
    # if x < z < y or y < z < x:  # if all numbers are the same -> returns None
    else:
        return z

def main():
    # reads 3 values as args
    x = int(input("What's x? "))
    y = int(input("What's y? "))
    z = int(input("What's z? "))

    # print the median
    print(median(x, y, z))

main()