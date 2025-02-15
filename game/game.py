import random

def main():

    n = random.randint(1, validate_level(True))
    while guess:= validate_guess(True): # not necessarily := input(..)
        if guess > n :
            print("Too Large!")
        elif guess == n:
            print("Just right!")
            break # why timed out??? 
        else:
            print("Too small!")


def validate_level(check):
    while check:
        try:
            # prompt level
            level = int((input("Level: ").strip()))
            return level if level > 0 else validate_level(True)
        except (ValueError, NameError):
            continue


def validate_guess(check):
    while check:
        try:
            #prompt guess
            guess = int(input("Guess: ").strip())
            return guess if guess > 0 else validate_guess(True)
        except (ValueError, NameError):
            pass

main()
