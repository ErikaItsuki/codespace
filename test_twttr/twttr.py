def main():

    word = shorten(input('Input: ').strip())
    print("Output:",word, end = "\n") # only this line is altered

def shorten(word):

    # loop -> if not vowel -> append string to formatted
    omit = ['e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in word:
        if char in omit:
            word = word.replace(char, "")

    return word

if __name__ == "__main__":
    main()

