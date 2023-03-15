import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)

def main():
    try:
