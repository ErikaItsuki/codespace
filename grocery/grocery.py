"""continue here
groceries = []

while True:
    try:
        item = input().rstrip().upper()
        groceries.append(item)
    except EOFError:
        for item in sorted(groceries):
            print(item)
        break

"""

#others
# Vwhile True: try ... then list.append()except EOFError: print() and break VVV
# output grocrey list .upper()V sorted by items

"""
1. Dunno if we need a dict for item (and the counter = ?)
    -->  counter put after case handling
    --> what if [name] and [number of item]?
    --> append()? after appending: can easily see how many item x in the list
        ==> how to "simplify into one item with some number?"

"""

