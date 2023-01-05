# starts with a hello (leading 5 chars)-> 0
# leading character = 'h' -> 20
# else-> 100

def main():
    greet = input("Greeting: ").strip().lower()
    greet_for_money(greet)

def greet_for_money(greet):
    print(greet.split())

main()






