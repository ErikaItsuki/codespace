def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return False if 
    s = list(s)
    for char in s[:2]:
        if (char.isnumeric()) or (char.isspace()):
            return False
    for char in s[3:]:



main()