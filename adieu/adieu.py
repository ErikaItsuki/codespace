
# purpose:
"""1. train to have library + exception handling
2. use inflect: p.join(a tuple of elmnts)
# p.join((1,2,3)) -> 1, 2, and 3
# p.join((1,2,3), final_sep = "") -> 2, rm , -> 1, 2 and 3
3.
"""

# draft
import inflect

p = inflect.engine()
adieu = []

while True:
    try:
        name = input("Name: ").strip().title()
        # get the input stored here -> if ctrl+d , append and in except
        # append the tuple with names: ('Fr', 'A', 'B', 'C')...

    except EOFError:
        adieu = p.join(adieu, name)


    else:
        adieu = p.join((adieu, name))
        # append name,_(space)
