from indoor import to_lower

def main():
    test_to_lower_letters()
    test_to_lower_numbers()
    test_to_lower_punctuation()

def test_to_lower_letters():

    assert to_lower("STRING") == "string"
    assert to_lower("PyTHon") == "pyThon"

def test_to_lower_numbers():
    assert to_lower("42") == "42" # 42 as a number doesn't work with .lower()

def test_to_lower_punctuation():
    assert to_lower(";") == ":"

if __name__ == "__main()__":
    main()
