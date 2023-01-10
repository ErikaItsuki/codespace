f.name = name
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        sel
    def __str__(self):
        return f"{self.name} says 'I do nothing~'" # saying thiswith self.name is valid
    ...

class Student(Wizard):
    def __init__(self,name,house): # still need the name as arg to be passed into the super/ parent class
        super().__init__(name)
        self.house = house

    def __str__(self):# nothing changed, still(self), by the way
        return f"{self.name} from {self.house}" # saying self.name with inherited super class

    ...

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"{self.name} teaches {self.subject}"
    ...

def main():
    wizard = Wizard("Ablus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defense Against the Dark Arts")
    print(student)
    print(professor)
    print(wizard)

if __name__ == "__main__":
    main()
