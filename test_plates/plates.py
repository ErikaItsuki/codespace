def main():
    ...


def is_valid(s):
    #check first 2 = alpha
    s = list(s)
    for i, char in enumerate(s):
        if char.isalpha() 

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

if __name__ == "__main__":
    main()