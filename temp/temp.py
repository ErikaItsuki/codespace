class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}" # seems self._name won't call the instance method once more
                                                # both having the same result

    @classmethod
    def get(cls):
        name = input("name: ").title()
        house = input("house: ").title()
        return cls(name, house) # will call __init__


    @property
    def name(self): # see __str__: f"{self.name}..." -> the self.name is taken for this
                    # why? becaue as we know self, which has self.name = name passed already,

        return self._name

    @name.setter
    def name(self, name): # self must be taken & name from the R of self.name = name
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

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()
