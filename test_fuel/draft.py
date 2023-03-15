import pytest

def f():
    return 3

def test_f():
    assert 1 % 2 == 0, "Value was odd, should be even"
    #output AssertionError: Value was odd, should be even

test_f()