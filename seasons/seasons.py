from datetime import date
import sys

# use classes

def main():
    print(date.today())
    yyyy, mm, dd = str(date.today()).split("-")
    print(yyyy, " ", mm, " ",  dd)

if __name__ == "__main__":
    main()


# taking date.today() by packaging:
# 1. str().split then convert to int
# 2. MORE EFFICIENT