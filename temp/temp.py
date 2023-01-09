def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    s = list(s)
    if 2 < (len(s)) < 6:
        for char in s[:2]:
            if (char.isnumeric()) or (char.isspace()):
                return False
        for char in s[3:]:
            if 

if __name__ == "__main__":
    main()