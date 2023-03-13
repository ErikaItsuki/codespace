def main():
    greeting = input("Greeting: ").strip().lower()
    print(value(greeting))

def value(greeting):
    amount = 0
    letters = list(greeting)
    if letters[0] == 'h':
        if letters[1:5] == ['e', 'l', 'l', 'o']:
            return amount
        else:
            amount = 20
    else:
        amount = 100
    return amount

if __name__ =="__main__":
    main()






