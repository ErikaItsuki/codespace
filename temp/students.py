import csv

students = []

with open("student.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append(row[0])


