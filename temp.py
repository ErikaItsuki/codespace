def main():
    string = input("camelCase: ") #ok
    camels = list(string) # ok
    to_snake_case(camels)

def to_snake_case(camels):
    snake = [] # syntax ok
    for i in range(len(camels)):
        if (camels[i].istitle()): # both is titla and isupper()are ok
                                # difference bwn these two:

            snake[i] = "_" + camels[i].lower()
        else:
            snake[i] = camels[i]
    return snake

main()


# insert()
# replace