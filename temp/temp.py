# purpose:
"""1. train to have library + exception handling
2.
3.
"""
# draft

adieu = "adieu, adieu, to "

while True:
    try:
        name = input("Name: ").strip().title()
        # get the input stored here -> if ctrl+d , append and in except

    except EOFError:
        adieu = adieu + ", and" + name

    else:
        adieu = adieu + ", " + name
        # append name,_(space)


