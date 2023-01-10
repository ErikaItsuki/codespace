with open("student.csv") as file:
    for line in file:
        row = line.rstrip().split(",") # row is not "listed" before,
                                       # but they are in csv
        print(f"{row[0]} is in {row[1]}")

# more effective to do:

