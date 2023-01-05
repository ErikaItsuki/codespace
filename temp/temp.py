# to write inputs to a file all at once:

with open("names.txt", "a") as file:
    for _ in range(3):
        name = input("What's your name? ")
        file.write(f"{name}\n")

