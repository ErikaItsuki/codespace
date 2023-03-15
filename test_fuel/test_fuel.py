from fuel import convert, gauge
import pytest
# running pytest: n passed means how many functions passed
# n relies no t=on the number of "assert" keywrd
# calling in main() is not the case

def test_convert():
    # good input
    assert convert("3/4") == round(3/4 * 100)

    # test boundaries
    assert convert("1/1") == 100
    assert convert("0/1") == 0

# To see whether a case has raised an err:
def test_convert_non_str():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("2/1")
        convert("-1/2")

def test_convert_divide_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(0.99) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


