with open("stuent.csv", "a") as file:
    for i in range(4):
        name = input("Name: ").strip().title()
        house = input("house: ").strip().title()
        file.write(f"{name},{house}\n")
