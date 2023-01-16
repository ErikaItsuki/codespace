"""
name = input().strip().upper()
 LIST OF DICT: fruit = {name : number}
 after number of each type of fruit counted: groceries = groceries.append(fruit)
1 APPLE
2 BANANA
1 TOMATO
"""
"""
# create 1 dict and append to list first:
counter = 0
number = 1

name = input("fruit: ")
fruit = {"name": name, "number": number}

fruit = {name : number}
"""
# no need to use list of dict, 1 dict is enough

# if name not in list.dict(): append (input("fruit"))
"""
grocery.append({name : 1})
# if equals -> grocery[name]+=1
grocery = {
    {input(): number},
    input(): number,
    input(): number,
    input(): number
}
"""
grocery = {}

while True:
    try:
        name = input().strip().upper()
        if name not in grocery.keys(): # .keys() for a single dict
            grocery[name] = 1 # append not for dict # the way to "append" a key
        else:
            grocery[name]+=1
    except EOFError:
        for item in grocery:
            # print(f"{item} {grocery[item]}") {item} = key: names
            print(f"{grocery[item]} {item}")
        break

