names = []

with open("names.txt") as file:
    new_name = input("the fourth name: ")
    file.write(f"{new_name}\n")
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")
