def main():
    chars = list(input("camelCase: "))
    for char in chars:
        print(char, end = "")

# string = "firstName"
# chars = list(string)

def convert(chars):
    for char in chars:
        if (char.istitle()): # both is titla and isupper()are ok
                                # difference bwn these two:

            char = "_"+char.lower()
        return chars

main()

# scope
# if else principles