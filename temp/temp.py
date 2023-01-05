name = input("What's your name? ")

with open("names.txt", "a") as file:
    for _ in range(3):
        file.write(f"{name}\n")

