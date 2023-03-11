from professor import get_level

def main():
    test_get_level()

def test_get_level(): #
    assert get_level() == 1
    assert get_level() == -1
    assert get_level() == 0


if __name__ == "__main__":
    main()