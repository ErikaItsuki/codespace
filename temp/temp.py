import random

class Hat:
    # sort the name to a house randomly
    def __init__(self): # remember it takes 1 arg (self) only
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses)) # I guess once the function has (self),
                                                         # it can have kinda "direct access" to some funcationality
                                                         # (like self.houses from __init__(self))

hat = Hat()
hat.sort("Harry")

