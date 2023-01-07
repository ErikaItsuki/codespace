def main():
    chars = list(input("camelCase: "))
    to_snake(chars)
    print()

def to_snake(chars):
    for char in chars:
        if (char.istitle()):
            char = "_"+ char.lower()
            print(char, end = "")
        else:
            print(char, end = "")




if __name__ == "__main__":
    main()



