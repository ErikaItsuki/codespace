import inflect

p = inflect.engine()

word = input("word: ").strip()
print("The plural of " ,word, "is ", p.plural(word))
print("Conditionally: ", word, "is ", p.plural("cat", 1))
#cat_count = 0/-ve -> cats
# input != cat -> input is cat
# if not the specified : print input is arg1
# else print arg1 is arg2

print(p)