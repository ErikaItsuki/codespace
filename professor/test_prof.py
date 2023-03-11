from professor import get_level

def main():
    test_get_level()

def test_get_level(): # I am afraid if assert get_level(sth input leading to reprompt) == get_level()
                      # will crash
    assert get_level() == 1

if __name__ == "__main__":
    main()