# When texting or tweeting,
# it’s not uncommon to shorten words to save time or space,
# as by omitting vowels,
# much like Twitter was originally called twttr.

def main():
    word = input("Input: ")
    print(omit_vowels(word))

def omit_vowels(string):

    #list of 2 : string and new formatted
    with_vowels = list(string)
    without_vowels = []
    # loop -> if not vowel -> append string to formatted
    for i in range(len(with_vowels)):
        if with_vowels[i] != 'a' or with_vowels[i] != 'e' or with_vowels[i] != 'i' or with_vowels[i] != 'o' or with_vowels[i] != 'u':
            without_vowels.append(with_vowels[i])




main()