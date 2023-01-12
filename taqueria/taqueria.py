menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0

 # :.2f, and should be the total so far

# ignore input != any of the items and ctrl d
while True:
    try:
        item = input("Item: ").strip().title()
        if item in list(menu):
            total += menu[item] # is item, not "item" inside []
                                # not necessarily in a for loop,
                                # as long as you have the keyName
            print(f"Total: ${total:.2f}")
        else:
            pass

    # avoid or catch any keyError
    except EOFError:
        print()
        break # seems that it doesn't create a newline autoly
