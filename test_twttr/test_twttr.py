from twttr import shorten

def test_default(word):
    assert shorten("") == ""


def test_with_vowels():
    ...

def test_without_vowels():
    ...


def test_numeric_without_vowels():
    ...

def test_numeric_with_vowels():
    ...