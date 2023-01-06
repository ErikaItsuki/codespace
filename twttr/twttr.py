# When texting or tweeting,
# it’s not uncommon to shorten words to save time or space,
# as by omitting vowels,
# much like Twitter was originally called twttr.

def main():
    word = input("Input: ")
    for letter in words:
        print(omit_vowels(letter))

def omit_vowels(string):

    #list of 2 : string and new formatted
    with_vowels = list(string)
    without_vowels = []
    # loop -> if not vowel -> append string to formatted
    for i in range(len(with_vowels)):
        if (with_vowels[i] != 'a' and
            with_vowels[i] != 'e' and
            with_vowels[i] != 'i' and
            with_vowels[i] != 'o' and
            with_vowels[i] != 'u'):
            # or is put at the end of each condition
            # new line conditions indented by 4, start the count from if (i = 1)
            # use paren if using new lines
            # or simply add a line of comment for distinction (still need to do the above)

            without_vowels.append(with_vowels[i])

    return without_vowels

main()