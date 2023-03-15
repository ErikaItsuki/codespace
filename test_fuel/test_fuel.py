from fuel import convert, gauge
import pytest
# running pytest: n passed means how many functions passed
# n relies no t=on the number of "assert" keywrd
# calling in main() is not the case

def test_convert():
    #assert convert("cat/dog") == test_convert_raises()
    assert convert("3/4") == round(3/4 * 100)
    assert convert("2/1") == None
    assert convert("-1/2") == None

    # test boundaries
    assert convert("1/1") == 100
    assert convert("0/1") == 0

# To see whether a case has raised an err:
def test_convert_non_str():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_convert_divide_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


