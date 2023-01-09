def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (whole(s) and digit_not_in_the_midst(s, counter(s))):
        return True
    else:
        return False

# check the whole string -> isspace(), (s.isnumeric() and not s.isdigit()) -> F
# 2 < x < 7 -> false
# check the whole string

def whole(s):
    s = list(s)
    if 2 < (len(s)) < 7:
        for char in s[0:2]:
            if not (char.isalpha()):
                return False
        for char in s[2:]:
            if not (char.isalpha() or char.isdigit()):
                return False
        return True
    # return None is no else -> is_valid will be false
    # potential danger??



# check numbers in the middle
# slice from the first number by a counter is much easier

def counter(s):
    counter = 0
    for char in s:
        if char.isalpha():
            counter+=1
        else:
            break
    return counter


# : if char.isdigit -> loop through till the end to see if isdigit too
# check if first no. = 0

def digit_not_in_the_midst(s, counter):
    result = True
    if counter != 6:
        if s[counter] == "0":
            result = False
        for char in s[counter:]:
            if not (char.isdigit()):
                result = False
                break
    return result


if __name__ == "__main__":
    main()
