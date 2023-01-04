#style # ***consistency within a module or function ***
# PEP 8:

# indentation
# tabs or spaces?
# maximum line length
# blank lines
# imports

#pip install pylint -> noisy
#pycodestyle -> reformat the code for you if it's a bit messy
#pip install black -> more popular now

students = {"Hermione" : "Griffindor", "Harry" : "Griffindor", "Ron" : "Griffindor", "Draco" = "Slytherin", "Padma" = "Ravenclow"}

for student in students:
    print(student, students[student])