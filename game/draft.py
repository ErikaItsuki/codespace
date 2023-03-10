import random

def main():

    n = random.randint(1, validate_level())

    if validate_guess() > n :
        print("Too Large")
    elif validate_guess() == n:
        print("just right")
    else:
        print("Too small")


    # prompt guess


def validate_level():
    while True:
        try:
            # prompt level
            level = int((input("Level: ").strip()))
            return level # main: n = randint(1, level)
        except (ValueError, NameError):
            pass



def validate_guess():
    while True:
        try:
            #prompt guess
            guess = int(input("Guess: ").strip())
            return guess
        except (ValueError, NameError):
            pass

main()
