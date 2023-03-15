import plates

def main():
    test_general_rules()
    test_is_valid()

def test_general_rules():
    assert plates.general_rules("CS50") == True


def test_is_valid():
    assert plates.is_valid("CS50") == True

if __name__ == "__main__":
    main()