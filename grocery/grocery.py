grocery = {}

while True:
    try:
        name = input().strip().upper()
        if name not in grocery.keys(): # .keys() for a single dict
            grocery[name] = 1 # append not for dict # the way to "append" a key
        elif not name:
            continue
        else:
            grocery[name]+=1
    except EOFError:
        for item in grocery:
            # print(f"{item} {grocery[item]}") {item} = key: names
            print(f"{grocery[item]} {item}")
        break

# use the item names as keys, values = counter
# to add in a key, name_of_existing_dict[new key] = the new key's value