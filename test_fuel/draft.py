import pytest

def f():
    return 3

def test_f():
    assert f() == 4

def test():
    assert 1 % 2 == 0, "Value was odd, should be even"
    #output AssertionError: Value was odd, should be even

test_f()
test()