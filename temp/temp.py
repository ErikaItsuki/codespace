class Student:
    def __init__(self, name, house):
        self.name = name # .name -> property of name
        self.house = house # .house -> property of house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self): # what is it for???
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def get_student():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house)


def main():
    student = get_student() # not Student(name, house) exactly
                            # get_student returns the value to be checked
                            # by the instance method (property)
                            # so if an error is rose, get_student()'s
                            # value won't be passed into student on the L
                            # student is an Obj
                            # = is kinda syntax to call a cons.
                            # get_student() here kinda helping call the cons
                            # cuz get_stu itself is not an instance method
                            # (it is outside Student !! )

    print(student) # here comes the purpose of __str__

if __name__ == "__main__":
    main()
