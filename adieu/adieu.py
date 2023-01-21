
# purpose:
"""1. train to have library + exception handling
2. use inflect: p.join(a tuple of elmnts)
# p.join((1,2,3)) -> 1, 2, and 3
# p.join((1,2,3), final_sep = "") -> 2, rm , -> 1, 2 and 3
3.
"""

# draft
import inflect
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
        print("Adieu, adieu, to " + p.join(tuple(names))) # np connect these two
                                                        # p.join convert a tuple to a string formatted
        break
