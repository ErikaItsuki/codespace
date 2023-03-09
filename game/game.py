import random

def main():
    validate()
    answer = random.randint(1, n)
    guess = int(input("Guess: "))
    if guess > answer:
        print("Too large")
    elif guess < answer:
        print("Too small")
    else:
        print("Just right")
        # quit

def validate():

    while True:
        try:
            n = int(input("Level: ")).strip()
            break
        except (ValueError, NameError):
            continue



main()