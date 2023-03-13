def main():
    print(is_valid("CS50"))


def is_valid(s):
    #check first 2 = alpha
    s = list(s)
    if s[0].isalpha() and s[1].isalpha():
        for i, char in enumerate(s[2:]):
            if char.isdigit():
                return check_digits("".join(s[i+2:]))

        return True
    else:
        return False

def general_rules(s): #DONE :)
    valid = True
    #check length
    s = list(s)
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


"""for j, digit in enumerate(s[i+1:]):
        if not s[i+1].isdigit():
            return False"""