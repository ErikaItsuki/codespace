from fuel import convert, gauge
import pytest

def main():
    test_convert()
    # test_gauge()

def test_convert():
    assert convert("cat/dog") == False
    assert convert("3/4") == round(3/4)
    assert convert("2/1") == False

def test_convert_raises():
    with pytest.raises(ValueError):
        test_convert()