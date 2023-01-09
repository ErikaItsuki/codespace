import random

class Hat: # use class, esp for real world entity

    # don't need a __init__

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # class var

    # and so sort(self)...

    def sort(self, name): # cls by convention : = ref of class
        print(name, "is in", random.choice(self.houses))

hat = Hat()
hat.sort("Harry")


