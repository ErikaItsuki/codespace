import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ").strip().title()
        if not name:
            continue
        else:
            names.append(name)
    except EOFError:
        print("Adieu, adieu, to " + p.join(tuple(names)))
        break
