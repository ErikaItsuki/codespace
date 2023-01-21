from twttr import shorten

def test_default(word):
    assert shorten("") == ""

def test_has_numeric():
    ...

def