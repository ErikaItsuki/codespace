with open("stuent.csv", "a") as file:
    for i in range(4):
        name = input("Name: ")
        house = input("house: ")
        file.write(f"{name}, {house}")
