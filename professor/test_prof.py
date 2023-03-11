from professor import get_level
from professor import generate_integer

def main():
    # test_get_level()
    test_generate_integer()

def test_get_level(): # I am afraid if assert get_level(sth input leading to reprompt) == get_level()
                      # will crash
    assert get_level() == 1

def test_generate_integer():

    assert generate_integer(2) == 10 #.
    assert generate_integer(3) == 100 #.

if __name__ == "__main__":
    main()