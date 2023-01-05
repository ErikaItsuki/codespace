def convert(string):
    return string.replace(":)", "🙂").replace(":(", "🙁")
    # only the 2 faces will be converted

def main():
    string = input()
    print(convert(string))

main()
