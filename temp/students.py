import csv

"""students = []

with open("student.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({name : house})

for student in sorted(students, key = lambda student: name):
    print(f"{name}, {house}")

"""
students = []

with open("student.csv") as file:
    # step 1: read the file and handle potential cases for you
    reader = csv.reader(file) # .reader() -> read what's inside the arg as a csv file
                              # and handle subtle danger
# iterate
    for row in reader:
        students.append({"name": row[0], "home": row[1]})
    """ unpacking:
    for name, home in reader: # row contains 2 var: name and house
        students.append


    """




for student in sorted(students, key = lambda student : student["name"]):
    print(f"{student['name']} is in {student['house']}")