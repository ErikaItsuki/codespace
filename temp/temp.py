class Student:
    def __init__(self, name, house):

        if not name:
            raise ValueError("missing name")

        self.name = name
        self._house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property # always for getter # why we need a getter: every code will be passed to setter to check
                                  # and so this getter, despite its syntax as a property, seems useless
    def house(self):
        return self._house

    @house.setter # syntax: @name_of_getter.setter
    def house(self, house): # two para

        if house not in ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    student.house = "number hour, Privet Drive" # this will also call the setter (to check as a "requirement")
                                                # Inside setter: if not 1 of 4 houses --> raise ValueError
    print(student)


def get_student():
    name = input("Name: ").title()
    house = input("House: ").title()
    return Student(name, house)


if __name__ == "__main__":
    main()

# self -> always pass as a REFERENCE of that Student Obj
# you give info in the terminal
