class Student:
    def __init__(self):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("What's your name? ")
    house = input("What's your name? ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()



# What he doing?!
# main
# get_student -> to initalize an obj from main, and return the whole student Obj
# inside get_student() -> Student(name, house) as a cons
#

# try to read the class only as type, other keeps the way to read funcitonal codes