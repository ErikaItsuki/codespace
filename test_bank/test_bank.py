import bank

def main():
    test_value_str()


def test_value_str():
    # test 'h'
    assert bank.value("hello") == 0
    assert bank.value("gello") == 20

def test_value_non_str():
    # non-str type
    assert bank.value(123) == 



if __name__ == "__main__":
    main()