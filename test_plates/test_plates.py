import plates

def main():
    test_is_valid()

def test_is_valid():
    """valid"""
    assert plates.is_valid("CS50") == True
    """invalid"""
    # len out of range
    # min 2 alphas
    # not accept char except alpha or digits
    # no numbers in the mid

def test_is_valid_length():
    # valid
    assert is_valid()

if __name__ == "__main__":
    main()