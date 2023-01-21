import inflect

p = inflect.engine()

"""names = ("A", "B", "C")
print(p.join(names)) # must have bracket inside

# ways to modify:
# 1. get a list -> copy to the list form the tuple -> modify the list -> change the list to a tuple

names = list(names) # valid
print("convertion succeed")

names = tuple(names) # valid
print("backward convertion succeed")"""

##### application #####
names = []
while True:
    try:
        name = input("Name: ").strip().title()
        names.append(name)
    except EOFError:
        print("adieu, adieu, to " + p.join(tuple(names))) # np connect these two
                                                        # p.join convert a tuple to a string formatted
        break


