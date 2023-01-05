#{:.1f}
# z cannot be 0
# expression is a str
def main():
    expression = input("Expression: ")
    math_interpreter(expression)

def math_interpreter(strings):

    x, y, z = strings.split(" ")
    x, z= float(x), float(z) # valid

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

