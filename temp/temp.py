students = []

with open("student.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


for student in sorted(students, key = lambda student : student["name"]):
    print(f"{student['name']} is in {student['house']}")

# lambda -> tell py this function has no name
# student -> a parameter : can use anything u want
# , but as we r calling every student in that list
# student ["name"] = return value