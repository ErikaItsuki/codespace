with open("student.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0] is in }")