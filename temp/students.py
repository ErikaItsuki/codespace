students = []

with open("student.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house" : house}
        students.append(student)

for student in sorted(students, key = lambda student: student["house"]):
    print(f"{student['name']} is in {student['house']}")

