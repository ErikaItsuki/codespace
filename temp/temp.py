import inflect

p = inflect.engine()

print(p.join(("A", "B", "C"))) # must have bracket inside

