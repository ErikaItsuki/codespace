# recreate a dict for sorted()

with open("student.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students, hey = lambda student: students(house)): # for each line : available arg = student, not students
                                                                        # return students(house)
    print(student)