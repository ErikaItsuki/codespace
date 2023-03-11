import random
levels = [1,2,3]

def main(): # if EEE x 3 --> display corr ans and prompt the nxt Q right away
    # level
    level = get_level()

    # 10 questions
    score = 0
    for i in range(10):
        x, y = generate_integer(level)
        print(f"{x} + {y} = ", end = "")

        # check each question
        question_chances = 0
        while question_chances < 3:
            answer = int(input(""))
            if answer != (x + y):
                question_chances += 1
                if question_chances > 2:
                    print(f"{x} + {y} = {x + y}")
                else:
                    print("EEE")
            else:
                score += 1
                break
    print(f"Score: {score}")



def get_level(): # DONE

    while True:
        try:
            level = int(input("Level: "))
            return level if level in levels else get_level() # don't else raise
        except ValueError:
            pass


def generate_integer(level): # returns a randomly geneated non-ve integer with level digits # ValueError if not 1, 2, 3

    lower = 10 ** (level - 1)
    upper = 10 ** level - 1
    if level == 1:
        x = random.randint(0, upper)
        y = random.randint(0, upper)
    elif level == 2 or level == 3:
        x = random.randint(lower, upper)
        y = random.randint(lower, upper)
    else:
        raise ValueError("level should be 1, 2, or 3")

    return x, y

def three_chances():
    chances = 0
    while chances < 3:
        try:
            answer = int(input(""))
        except ValueError:
            print("EEE")
            chances += 1
        else:
            if answer != x + y:
                continue
            else:
                return ...

if __name__ == "__main__":
    main()

