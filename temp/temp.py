class Student:
    def __init__(self, name, house):

        if not name:
            raise ValueError("missing name")

        self.name = name
        self.house = house # dont add an underscore here
                           # cuz you want the value to be checked (from get_stu() input)

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter # usually put right under that property
    def name(self, name):
        if not name: # or if name == ""
            raise ValueError("Missing name")
        self._name = name

    @property # always for getter
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
