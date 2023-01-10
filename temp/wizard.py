class Student:
    def __init__(self, name ,house):
        self.name = name
        self.house = house

    ...

class Professor:
    def __init__(self, name, subject):
        self.name = name #repeated
        self.subject = subject

    ...

class Wizard: # define a class with common features

# to achieve inheritance
# tell python they are linked : class Student(Wizard) # (super class)
# but when a student __init__ will be called for an Student obj, which also needs
# __init__ from the super class: super()._init_(name) -> access super, call__init__, and
# pass the student name arg to the super class as an arg
