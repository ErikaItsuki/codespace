students = []

with open("student.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name # create a key for dict repr name of students
        student["house"] = house # same as above
        students.append(student)



for student in sorted(students, key = ):
    print(student)