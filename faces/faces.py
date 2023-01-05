def convert(string):
    return string.replace(":)", "🙂").replace(":(", "🙁")
    # only the 2 faces will be converted
    # seemingly, if nothing matches the 1st arg in replace -> ignored

def main():
    string = input()
    print(convert(string))

main()
