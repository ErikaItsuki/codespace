
string = "firstName"
chars = list(string)

for char in chars:
    if (char.istitle()): # both is titla and isupper()are ok
                               # difference bwn these two:

        char = "_"+char.lower()
    print(char, end ="")



