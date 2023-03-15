def main():
    plate = list(input("Plate: "))
    if general_rules(plate) and is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #check first 2 = alpha
    if s[0].isalpha() and s[1].isalpha():
        for i, char in enumerate(s[2:]):#how about CS
            if char.isdigit():
                return check_digits("".join(s[i+2:])) if char != '0' else False

        return True
    else:
        return False

def general_rules(s): #DONE :)
    valid = True
    #check length
    if 2 <= len(s) <= 6:
        i = 0
        while i < len(s):
            if not (s[i].isalpha() or s[i].isdigit()):
                return False
            else:
                i += 1
    else:
        valid = False
    return valid

def check_digits(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
