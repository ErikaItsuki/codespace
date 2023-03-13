def main():
    greeting = input("Greeting: ").strip().lower()
    value(greeting)

def value(greeting):
    letters = list(greeting)
    if letters[0] == 'h':
        if letters[1:5] == ['e', 'l', 'l', 'o']:
            print(0)
        else:
            print(20)
    else:
        print(100)

if __name__ =="__main__":
    main()






