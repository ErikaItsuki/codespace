class Student:
    ...# to be impleented later

def get_student():
    student = Student() # looks like creating an obj
                        # student(lowercase) is the obj
                        # Student() is the  which we can access stuff in the clas
    student.name = input("Name: ")
    student.house = input("house: ")
    return student
