def main():
    plate = list(input("Plate: "))
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    valid = True
    if 2 <= len(s) <= 6:
        for i, char in enumerate(s[0:2]): # when i = 2 quit (same as)
            if not char.isalpha():
                valid = False
        for i, char in enumerate(s[2:]):
            if char.isalpha():
                pass
            elif char.isdigit() and char != '0':
                try:
                    # take the string to int from i
                    digits = 
                    int("".join(s[i:]))
                except ValueError:
                    raise ValueError("has digit(s) in the middle")
            else:
                valid = False
    else:
        return False
    return valid

if __name__ == "__main__":
    main()
