#{:.1f}
# z cannot be 0
# expression is a str
def main():
    expression = input("Expression: ")
    print(math_interpreter(expression))

def math_interpreter(strings):

    x, y, z = strings.split(" ")
    x = float(x)
    z = float(z)

    if y == '+':
        print(f"{x + z:.1f}")
    elif y == '-':
        print(f"{x - z:.1f}")
    elif y == '*':
        print(f"{x * z:.1f}")
    elif y == '/' and z != 0:
        print(f"{x / z:.1f}")

main() # math_interpreter has no return value:
       # when exit and just before main is called,
       # (return) main: None

