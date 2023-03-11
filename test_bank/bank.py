def main():
    greet = input("Greeting: ").strip().lower()
    greet_for_money(greet)

def greet_for_money(greet):
    letters = list(greet)
    if letters[0] == 'h':
        if letters[1:5] == ['e', 'l', 'l', 'o']:
            print("$0")
        else:
            print("$20")
    else:
        print("$100")

main()






