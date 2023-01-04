
string = "firstName"
chars = list(string)

# change char to lower

for char in chars:
    if (char.istitle()): # both is titla and isupper()are ok
                               # difference bwn these two:

        char = "_"+char.lower()
    print(char, end ="")




for char in chars:
    if char.istitle() == True:
        char = "_"+char.lower()

print(chars) # scope?? WHY NOT WORKING OUTSIDE
"""

