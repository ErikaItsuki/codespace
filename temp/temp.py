def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# def is_valid(s):


def only_letters_and digits(s):
    s = list(s)
    if 2 < (len(s)) < 6:
        for char in s:
            if (char.isnumeric()) or (char.isspace()):
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()

"""cache

for char in s[3:]:
            if (char.isdigit()):
                ...
            else (char.is)


"""

# no spaces
# 2 < x < 6
# no no. in the midst
# at least 2 char