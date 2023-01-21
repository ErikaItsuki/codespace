import random

class Hat:
    houses = ["G", "H", "R", "S"]
    @classmethod
    def sort(cls, name):
        print(name, "is in ", random.choice(cls.houses))

Hat.sort("Harry") # directly calling the function