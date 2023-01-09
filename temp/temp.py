def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #
    ...
# check the whole string -> isspace(), (s.isnumeric() and not s.isdigit()) -> F
# 2 < x < 6 -> not = F

# check the whole string

def whole(s):
    s = list(s)
    if 2 < (len(s)) < 6:
        for char in s[0:2]:
            if not (char.isalpha()):
                return False
        for char in s[2:]:
            if not (char.isalpha() and char.isdigit()):
                return False
            return True


# check numbers in the middle
# slice from the first number is much easier

def digit_not_in_the_midst(s, counter):
    result = True
    for char in s[counter:]:
        if not (char.isdigit()):
            result = False
            break
    return result

def counter(s):
    counter = 0
    for char in s:
        if char.isalpha():
            counter+=1
        else:
            return counter


def first_number(s):
    for char in s[2:]:
        if char.isdigit():



# : if char.isdigit -> loop through till the end to see if isdigit too
# check if first no. = 0


# easy to KO:

"""
for char in s:
    if char.isspace():
        false
"""
"""
if (s.isnumeric() and not s.isdigit()):
    false
"""

"""
def only_letters_and digits(s):
    s = list(s)
    if 2 < (len(s)) < 6:
        for char in s:
            if (char.isnumeric()) or (char.isspace()):
                return False
        return True
    else:
        return False
"""
if __name__ == "__main__":
    main()

"""cache

for char in s[3:]:
            if (char.isdigit()):
                ...
            else (char.is)


"""

#[0-2 are must, :]
# if it starts to be a digit (if char.isdigit() and char != 0-> do sth)
# all comers should be digits
# sth =
