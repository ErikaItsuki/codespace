import inflect

p = inflect.engine()

word = input("word: ").strip()
print("The plural of " ,word, "is ", p.plural(word))