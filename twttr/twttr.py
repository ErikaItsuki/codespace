def main():

    words = omit_vowels(input('Input: ').strip())
    print(words, "\n")

def shorten(word):

    # loop -> if not vowel -> append string to formatted
    omit = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in with_vowels:
        if char in omit:
            with_vowels = with_vowels.replace(char, "")

    return with_vowels

if __name__ == "__main__":
    main()

