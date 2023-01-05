# prog exits -> things stored are lost
# (that's why u need to type python .py python .py again and again)

names = []

for _ in range(3):
    names.append(input("What's your name? "))

# sort a list in a loop
for name in sorted(names):
    print(f"hello, {name}")
