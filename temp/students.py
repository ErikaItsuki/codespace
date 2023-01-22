import csv

students = []

with open("student.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({name : house})

for student in sorted(students, key = lambda student: name):
    print(f"{name}, {house}")


