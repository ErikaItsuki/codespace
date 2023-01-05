name = input("what's your name? ")

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello, ", line)

