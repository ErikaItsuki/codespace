import plates

def main():
    test_general_rules()

def test_general_rules():
    assert plates.general_rules("CS50") == True

if __name__ == "__main__":
    main()