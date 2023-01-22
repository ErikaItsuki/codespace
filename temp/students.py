import csv

students = []

with open("student.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({row[0]:row[1]})

for student in sorted(students, key = lambda student: row[0]):
    print(f"{row[0]}, {row[1]}")


