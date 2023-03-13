import bank

def main():
    test_value_h()
    test_value_str()
    test_value_non_str()


def test_value_h():
    # test 'h'
    assert bank.value("hello") == 0
    assert bank.value("gello") == 20

def test_value_str():
    assert bank.value("ello") == 100
    assert bank.value("@#$%^&*()") == 100

def test_value_non_str():
    # non-str type
    assert bank.value(123) == 100

if __name__ == "__main__":
    main()