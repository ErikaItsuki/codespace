from temp import hello


def test_hello():
    assert hello() == "hello, world"
    assert hello("David") == "hello,David"

