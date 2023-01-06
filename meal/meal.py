# not time for meal -> no output


# convert a string  of : to .
# time <= 24.0
def main():
    time = input("What time is it? ")
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")

def convert(time):
    hours, minute = time.split(":")
    number = int(hours) + int(minute)/60
    return number


if __name__ == "__main__":
    main()
