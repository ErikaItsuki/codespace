# When texting or tweeting,
# it’s not uncommon to shorten words to save time or space,
# as by omitting vowels,
# much like Twitter was originally called twttr.

def main():

    words = list(omit_vowels(input("Input: ").strip()))
    for word in words:
        print(word, end = "")
        print()

def omit_vowels(with_vowels):

    without_vowels = []
    # loop -> if not vowel -> append string to formatted
    for i in range(len(with_vowels)):
        if ((with_vowels[i] != 'a' and with_vowels[i] != 'A') and
            (with_vowels[i] != 'e' and with_vowels[i] != 'E') and
            (with_vowels[i] != 'i' and with_vowels[i] != 'I') and
            (with_vowels[i] != 'o' and with_vowels[i] != 'O') and
            (with_vowels[i] != 'u' and with_vowels[i] != 'U')):
            # or is put at the end of each condition
            # new line conditions indented by 4, start the count from if (i = 1)
            # use paren if using new lines
            # or simply add a line of comment for distinction (still need to do the above)

            without_vowels.append(with_vowels[i])

    return without_vowels

main()