import random

class Hat: # use class, esp for real world entity

    # don't need a __init__

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # class var

    # and so sort(self), but @class method
    @classmethod
    def sort(cls, name): # cls by convention : = ref of class
        print(name, "is in", random.choice(cls.houses))

# no longer need to create an Obj
Hat.sort("Harry") # capitalize the 'h' -> indicating class variable


