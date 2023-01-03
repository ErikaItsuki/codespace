string = "firstName"
# chars = string.split() # change into a list
chars = list(string)
print(chars)

for char in chars:
    if char.



"""
for char in chars:
    if char.istitle() == True:
        char = "_"+char.lower()

print(chars)
"""
"""
for char in chars:
    if char.isupper():
        char = "_" + char.lower()

for char in chars:
    print(char)

"""

# .split(sep=None, maxsplit=- 1) : separate the string into chunks
# if you need to sep by char, use .list()