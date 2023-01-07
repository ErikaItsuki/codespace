from calculator import square

def test_square():
    assert square(2) == 4 # unsure but i guess assert takes square(2) and 4
                           # to be the "arg"-> assert (True/False) -> and assert
                           # is meant to return a boolean
    assert square(-3) == 9
    assert square(0) == 0
