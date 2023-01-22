# recreate a dict for sorted()

students = []

with open("student.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house" : house}
        students.append(student)

for student in sorted(students, key = lambda student: student["house"]): # for each line : available arg = student, not students
                                                                        # return students(house)
    print(f"{student['name']} is in {student['house']}")

# common mistakes on using dict
# 1. student["key"] -> [] and ""
# 2. use '' in an fstring with keys
# 3. sorted is for list
# 4. can sort a dict, so students = [] is not a must

students = {}

with open("student.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students[name] = house

for student in sorted(students.keys()):
    print(f"{student} is in {students[name]}")
