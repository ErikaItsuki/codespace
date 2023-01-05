class Student:
    def __init__(self): # instance method: designed by the author of py
                        # if you want to initialize the contents of an obj of a class
                        # you do this :)
        self.name = name
        


def main():
    student = get_student() #student = obj ???
    print(f"{student.name} from {student.house}")

def get_student():
    # instead of creating an obj for attr
    # it's more powerful : increase correctness
    name = input("Name: ")
    house =input("House: ")
    student = Student(name, house) # constructor
    return student

if __name__ == "__main__":
    main()
