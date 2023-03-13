import bank

def main():
    test_value_upper()
    test_value_h()
    test_value_str()
    test_value_non_str()

def test_value_upper():
    assert bank.value("HELLO") == 0
    assert bank.value("GEllo") == 100


def test_value_h():
    # test 'h'
    assert bank.value("hello") == 0
    assert bank.value("hey") == 20
    assert bank.value("gello") == 100

def test_value_str():
    assert bank.value("ello") == 100
    assert bank.value("@#$%^&*()") == 100

def test_value_non_str():
    # non-str type
    assert bank.value(str(123)) == 100 # input in main converted into str

if __name__ == "__main__":
    main()