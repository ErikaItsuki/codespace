#{:.1f}
# z cannot be 0
# expression is a str
def main():
    expression = input("Expression: ")
    print(math_interpreter(expression))

def math_interpreter(string):

    x, y, z = string.split(" ")
    float(x)
    float(z)

    if y == '+':
        print(f"{x + z:.1f}")
    elif y == '-':
        print(f"{x + z:.1f}")
    elif y == '*':
        print(f"{x + z:.1f}")
    elif y == '/':
        print(f"{x + z:.1f}")

main()
