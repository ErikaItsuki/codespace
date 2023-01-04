def main():
    string = input("camelCase: ") #ok
    camels = list(string) # ok
    snake_case = to_snake_case(camels)
    for snake in snake_case:
        print(snake, end = "")

def to_snake_case(camels):
    snake = [] # syntax ok # len = 0 -> list assignment index out of range -> use append instead
    for camel in camels:
        if (camel.istitle()): # both is titla and isupper()are ok
                                # difference bwn these two:

            snake.append("_" + camel.lower())
        else:
            snake.append(camel)
    return snake

main()


# insert()
# replace