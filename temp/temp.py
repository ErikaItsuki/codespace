# Vwhile True: try ... then list.append()except EOFError: print() and break VVV
# output grocrey list .upper()V sorted by items

"""
1. Dunno if we need a dict for item (and the counter = ?)
    -->  counter put after case handling
    --> what if [name] and [number of item]?
    --> append()? after appending: can easily see how many item x in the list
        ==> how to "simplify into one item with some number?"

"""

groceries = []

while True:
    try:
        item = input().rstrip().upper()
        groceries.append(item)
    except EOFError:
        groceries = sorted(groceries)
        break
    #else: # but if nothing goes wrong , go ahead and do this (else)

#printing the list after sorting
for i in range(len(groceries)):
    if groceries[i] == groceries[i-1]:
        counter += 1
    else:
        print(f"{i} {groceries[i-1]}")
        counter = 1
# output:
# 0 TOMATO
# 3 APPLE
# 7 BANANA

""" failed case 0: very hard to use dict -> look for dict sol (discord)!!
#for grocery in groceries:
#   grocery = {"item": grocery, "number" = 1}


# get the list sorted beforehand!!

def counter(items):
    i = 1
    while (i <= len(groceries)):
        if groceries[i] == groceries[i-1]:
            i += 1
        else:
            return i

grocery = {"item" : grocery, "number": counter(groceries)}


"""


""" Failed case 1
groceries = []

while True:
    try:
        item = input().strip().upper()
        grocery = {"item" : item, "number": 1}
        if item == # well, separated into different loops and so hard to access the previous' keys


"""
