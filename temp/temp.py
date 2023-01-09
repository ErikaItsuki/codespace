# classes saw in lec

"""
1. int
2. str
3. list
4. dict
...
"""
# class method != instance method (by default)
# function of a class # function for an obj
# @classmethod -> e.g. 1 functionality

class Hat:
    def sort(self, name):
        print(name, "is in", "some house") # "some house" : not knowing what to
                                           # do yet, but as a placeholder

hat = Hat()
hat.sort("Harry") # then you know what to do for ...:
                  # sort a name to print name's house

# test these 5 lines -> easier to handle if u r wrting big prg