# prompt math question
# if right: prompt nxt Q
# else: print EEE (counter of ame problem++)
# if counter >= 3: print correct answer
import random # generate total 10 Q (fixed), X + Y = ..., X and Y use randint
levels = [1,2,3]

def main():
    validate_level(True)




def validate_level(check):
    while check:
        try:
            level = int(input("Level: "))
            return level if level in levels else validate_level(True)
        except ValueError:
            pass

main()