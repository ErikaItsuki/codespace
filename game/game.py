import random

def main():

    while True:
        try:
            n = int(input("Level: ").strip())
            break
        except (ValueError, NameError):
            continue
    answer = random.randint(1, n)
    guess = int(input("Guess: "))
    while True:
        if guess > answer:
            print("Too large")
            guess = int(input("Guess: "))
        elif guess < answer:
            print("Too small")
            guess = int(input("Guess: "))
        else:
            print("Just right")
            break

main()