students = []

with open("student.csv")as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

# students[0] = "Hermione is in Gryffindor"
# and so forth
# combining the name and house into one element by a fstring
