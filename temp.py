def main():
    camels = list(input("camelCase: "))
    to_snake_case(camels)

def to_snake_case(camel_case):
    snake = []
    for i in camels:
        if (camels[i].istitle()): # both is titla and isupper()are ok
                                # difference bwn these two:

            snake[i] = "_" + camels.lower()
        else:
            snake[i] = camels[i]
    return snake

main()
