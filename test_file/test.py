import power

def main():
    test_power()

def test_power():
    assert power.power(2) == 4
    assert power.power(2) == 5

if __name__ == "__main__":
    main()