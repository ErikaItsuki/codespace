from twttr import shorten

def test_default(word):
    assert shorten("") == ""


def test_with_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""

def test_without_vowels():
    assert("") == ""


def test_numeric_without_vowels():
    ...

def test_numeric_with_vowels():
    ...