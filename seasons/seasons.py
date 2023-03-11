from datetime import date
import sys

# use classes

def main():
    print(date.today())
    yyyy, mm, dd = date.today().split('-')

if __name__ == "__main__":
    main()