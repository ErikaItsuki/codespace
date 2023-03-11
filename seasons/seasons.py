from datetime import date
import sys

# use classes

def main():
    print(date.today())
    yyyy, mm, dd = str(date.today()).split("-")
    print(yyyy, " ", mm, " ",  dd)

if __name__ == "__main__":
    main()