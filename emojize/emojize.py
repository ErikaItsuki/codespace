import emoji

input = input("Input: ").strip()
#input = input.replace("", ":") # and remember: cuz replace returns a copy of the original str
                              # if you want to use the same str_name, you have to assign it
                               # to the var of origin
input = ":"+ input +":"
print(input)

