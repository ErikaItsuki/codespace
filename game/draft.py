import random

def main():
#while True:
    while True:
        try:
    # prompt level
            level = int((input("Level: ").strip()))
        except (ValueError, NameError):
            continue
        else:
            n = random.randint(1, level)
            guess = int(input("Guess: ").strip())
            if guess > n :
                return f"Too Large"
            elif guess == n:
                return f"just right"
            else:
                return f"Too small"


    # prompt guess

main()

def validate_level():
    while True:
        try: 

def validate_guess():
