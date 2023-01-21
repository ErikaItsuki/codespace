def main():

    words = omit_vowels(input('Input: ').strip())
    print(words, "\n")

def omit_vowels(with_vowels):

    # loop -> if not vowel -> append string to formatted
    omit = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in with_vowels:
        if char in omit:
            with_vowels = with_vowels.replace(char, "")

    return with_vowels

if __name__ == "__main__":
    main()


"""NOTES
line13
# new line conditions indented by 4, start the count from if (i = 1)
# use paren if using new lines
# or simply add a line of comment for distinction (still need to do the above)
"""