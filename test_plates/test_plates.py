from plates import is_valid

def test_CS50():
    assert is_valid("CS50") == True

def test_is_valid_length():

    assert is_valid("CSSSSS") == True
    assert is_valid("CSSSSSC") == False
    assert is_valid("C") == False

def test_is_valid_min_2_alphas():

    assert is_valid("CS") == True
    assert is_valid("CSS") == True
    assert is_valid("C22222") == False

def test_is_valid_mid_nums():

    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False

def test_is_valid_numeric():
    assert is_valid("CS.50") == False
