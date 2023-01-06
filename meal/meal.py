# not time for meal -> no output


# convert a string  of : to .
# time <= 24.0
def main():
    print(convert(input("What time is it? ")))

def convert(time):
    hours, minute = time.split(":")
    number = int(hours) + int(minute)/60
    if 7 <= number <= 8:
        meal = "breakfast time"
    elif 12 <= number <= 13:
        meal = "lunch time"
    elif 18 <= number <= 19:
        meal = "dinner time"
    else:
        
    return meal


if __name__ == "__main__":
    main()
