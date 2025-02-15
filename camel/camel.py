def main():
    camels = list(input("camelCase: "))
    snake_case = to_snake_case(camels)
    for snake in snake_case:
        print(snake, end = "")

def to_snake_case(camels):
    snake = [] # .append() is always used after a LIST, never a string
    for camel in camels:
        if (camel.istitle()):
            snake.append("_" + camel.lower())
        else:
            snake.append(camel)
    return snake

main()
