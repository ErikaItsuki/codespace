class Student:
    ...# to be implemented later

def main():
    student = get_student() #student = obj ???
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student() # creating an obj
                        # student(lowercase) is the obj
                        # Student() is the  which we can access stuff in the clas
    student.name = input("Name: ")
    student.house = input("house: ")
    return student

if __name__ == "__main__":
    main()
