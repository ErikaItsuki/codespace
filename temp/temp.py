
#🙂🙁 from emojipedia

def convert(string):
    string.replace(":)", "🙂")
    
    # only the 2 faces will be converted

def main():
    string = input()
    print(convert(string))

main()