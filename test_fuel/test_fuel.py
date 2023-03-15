from fuel import convert, gauge
import pytest

def main():
    test_convert()
    # test_gauge()

def test_convert():
    #assert convert("cat/dog") == test_convert_raises()
    assert convert("3/4") == round(3/4 * 100)
    #assert convert("2/1") == None

# To see whether a case has raised an err:
def test_convert_raises():
    with pytest.raises(ValueError):
        convert("cat/dog")
