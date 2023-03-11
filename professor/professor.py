import random
levels = [1,2,3]

def main(): # if EEE x 3 --> display corr ans and prompt the nxt Q right away
    # level
    level = get_level()

    # 10 questions
    score = 0
    for i in range(10):
        x, y = generate_integer(level)

        # check each question
        if check_answer_in_three(x, y):
            score += 1
        else:
            print(f"{x} + {y} = {x + y}")

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

def check_answer_in_three(x, y):
    chances = 0
    while chances < 3:
        try:
            answer = int(input(f"{x} + {y} =")) # can?
        except ValueError:
            print("EEE")
            chances += 1
            # continue # if not -> not checked in while condition and ... may wait forever
        else:
            if answer != x + y:
                chances += 1
                continue
            else:
                return True
    return False

if __name__ == "__main__":
    main()

