# starts with a hello (leading 5 chars)-> 0
# leading character = 'h' -> 20
# else-> 100

def main():
    greet = input("Greeting: ").strip().lower()
    greet_for_money(greet)

def greet_for_money(greet):
    letters = list(greet)
    if letters[0] == 'h':
        #if letters[1] == 'e' and letters[2] == 'l' and letters [3] == 'l' and letters[4] == 'o':
        # SO terribly long!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if letters[1:5] == ['e', 'l', 'l', 'o']:
            print("$0")
        else:
            print("$20")
    else:
        print("$100")

main()






