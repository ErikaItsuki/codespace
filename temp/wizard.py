class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...

class Student(Wizard):
    def __init__(self,name,house): # still need the name as arg to be passed into the super/ parent class
        super().__init__(name)
        self.house = house

    ...

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

    ...

def main():
    wizard = Wizard("Ablus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defense Against the Dark Arts")

if __name__ == "__main__":
    main()

# to achieve inheritance -> do 2 things
# tell python they are linked : class Student(Wizard) # (super class)
# but when a student __init__ will be called for an Student obj, which also needs
# __init__ from the super class: super()._init_(name) -> access super, call__init__, and
# pass the student name arg to the super class as an arg -> very similar to Student.get(arg)
