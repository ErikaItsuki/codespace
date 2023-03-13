def main():
    ...


def is_valid(s):
    ...

def general_rules(s):
    valid = True
    #check length
    s = list(s)
    if 2 <= len(s) <= 6:
        i = 0
        while i < len(s):
            if s[i] != (s[i].isalpha() or s[i].isdigit()):
                return False
            else:
                i += 1

    else:
        valid = False
    return valid

if __name__ == "__main__":
    main()