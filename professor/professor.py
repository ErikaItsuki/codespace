# prompt math question
# if right: prompt nxt Q
# else: print EEE (counter of ame problem++)
# if counter >= 3: print correct answer
import random # generate total 10 Q (fixed), X + Y = ..., X and Y use randint
levels = [1,2,3]
score = 0
questions = 0

def main(): # if EEE x 3 --> display corr ans and prompt the nxt Q right away
    # level = validate_level(True)
    x, y = generate_integer(get_level())
    print(x, y)
"""    while questions < 10:
        # do 10 questions
        questions += 1
    ..."""


def get_level(): # DONE
    while True:
        try:
            level = int(input("Level: "))
            return level if level in levels else get_level() # don't else raise
        except ValueError:
            pass


def generate_integer(level): # returns a randomly geneated non-ve integer with level digits # ValueError if not 1, 2, 3

    lower = digit = 10 ** (level - 1)
    upper = 10 * level - 1
    if level == 1:
        x = random.randint(0, upper)
        y = random.randint(0, upper)
    elif level == 2 or level == 3:
        x = random.randint(lower, upper)
        y = random.randint(lower, upper)
    else:
        raise ValueError("level should be 1, 2, or 3")

    return x, y
    # 1 -> 1 - 9
    # 2 -> tens
    # 3 -> hundreds
    ...



if __name__ == "__main__":
    main()

