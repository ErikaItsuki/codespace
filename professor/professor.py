# prompt math question
# if right: prompt nxt Q
# else: print EEE (counter of ame problem++)
# if counter >= 3: print correct answer
import random # generate total 10 Q (fixed), X + Y = ..., X and Y use randint
levels = [1,2,3]
score = 0

def main():
    level = validate_level(True)





def get_level(check): # for n digits
    while check:
        try:
            n = int(input("Level: "))
            return n if level in levels else validate_level(True)
        except ValueError:
            pass

main()