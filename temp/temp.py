def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# check the whole string -> isspace(), (s.isnumeric() and not s.isdigit()) -> F
# 2 < x < 6 -> not = F

# check the whole string for spaces, punctuations, and its length

def whole(s):
    s = list(s)
    if 2 < (len(s)) < 6:
        for char in s:
            if (char.isspace()) or (char.isnumeric() and not char.isdigit()):
                return False
            return True
    return False

def first_two_are_letters(s):

    for char in s[0:2]:
        if 


# check front 2 chars
# check numbers in the middle : if char.isdigit -> loop through till the end to see if isdigit too
# check if first no. = 0





def is_valid(s):
    ...

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
