def main(): # encouraged to be at the top if not in another file

    student = Student.get()
    print(student)

######
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls): #by nature
        name = input("name: ").title()
        house = input("house: ").title()
        return cls(name, house)

    @property
    def name(self):

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
#######
if __name__ == "__main__":
    main()
