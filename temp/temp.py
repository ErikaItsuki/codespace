def main():
    chars = list("firstName")
    print(to_snake(chars))

def to_snake(chars):
    for char in chars:
        if (char.istitle()):
            char = "_"+ char.lower()

    return chars

if __name__ == "__main__":
    main()



