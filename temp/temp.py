def main():

    words = omit_vowels(input('Input: ').strip())
    print(words, "\n")

def omit_vowels(with_vowels):

    without_vowels = []
    # loop -> if not vowel -> append string to formatted
    omit = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(with_vowels)):
        if with_vowels[i] not in omit:

            without_vowels.append(with_vowels[i])

    return without_vowels

if __name__ == "__main()__":
    main()

