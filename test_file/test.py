import square

def main():
    test_squared()

def test_squared():
    assert squared(2) == 4
    assert squared(2) == 5

if __name__ == "__main__":
    main()