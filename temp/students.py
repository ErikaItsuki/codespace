# recreate a dict for sorted()

students = []

with open("student.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house" = house}
        students.append(student)

for student in sorted(students, hey = lambda student: student(house)): # for each line : available arg = student, not students
                                                                        # return students(house)
    print(student)