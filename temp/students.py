with open("students.csv", "r") as file:
    for line in file:
        name, house = line.split(",")
        print(f"{name} is in {house}")