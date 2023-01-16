# to-do : debug !!

grocery = {}

while True:
    try:
        name = input().strip().upper()
        if not name:
            continue
        elif name not in grocery.keys(): # .keys() for a single dict
            grocery[name] = 1 # append not for dict # the way to "append" a keynot name:
        else:
            grocery[name]+=1
    except EOFError:
        for item in sorted(grocery, key = lambda grocery: name): # sorted for both list and dict
        # for item in grocery stays the same: tortilla comes before sweet potato
            # print(f"{item} {grocery[item]}") {item} = key: names
            print(f"{grocery[item]} {item}")
        break

# use the item names as keys, values = counter
# to add in a key, name_of_existing_dict[new key] = the new key's value
# for "" is not the first input, the first if statement includes elif not name
# -> order matters VVV