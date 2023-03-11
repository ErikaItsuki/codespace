# prompt math question
# if right: prompt nxt Q
# else: print EEE (counter of ame problem++)
# if counter >= 3: print correct answer
import random # generate total 10 Q (fixed), X + Y = ..., X and Y use randint
levels = [1,2,3]
score = 0

def main(): # if EEE x 3 --> display corr ans and prompt the nxt Q right away
    level = validate_level(True)



def get_level(check): # for n digits
    while check:
        try:
            level = int(input("Level: "))
            return level if level in levels else get_level(True)
        except ValueError:
            pass

def generate_integer(level):
    # 1 -> 1 - 9
    # 2 -> tens
    # 3 -> hundreds



if __name__ == "__main__":
    main()