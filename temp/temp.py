class Student:
    def __init__(self): # instance method: designed by the author of py
                        # if you want to initialize the contents of an obj of a class
                        # you do this :)
        self.name = name
        self.house = house
        # the funciton will always be called, by definition of how py classes work
        #
        # then what is for self : gives to access to the obj u have currently created
        # "self" is the convention: u can call anything

        # difference between __init__ and a default constructor
        # called initialization method in py
        # __new__ to construct an (empty) Obj in memory and
        # __init__ to initialize -> because py generally does the other part for u,
        # __init__ is uually the only thing you have to worry 'bout



def main():
    student = get_student() #student = obj ???
    print(f"{student.name} from {student.house}")

def get_student():
    # instead of creating an obj for attr
    # it's more powerful : increase correctness
    name = input("Name: ")
    house =input("House: ")
    student = Student(name, house) # constructor call
    return student

if __name__ == "__main__":
    main()

#concept:
# name = attributes in a class
# self.name = instance variable