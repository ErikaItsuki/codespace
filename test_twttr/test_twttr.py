from twttr import shorten

def test_default():
    assert shorten("") == ""


def test_with_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""

def test_without_vowels():
    assert("hmm") == "hmm"


def test_numeric_without_vowels():
    assert shorten("hmm_1") == "hmm_1"
    assert shorten("apple, ") == "ppl, "

def test_numeric_with_vowels():
    assert shorten("apple_1") == "ppl_1"
    assert shorten("Apple_1") == "ppl_1"

def with_y():
    assert shorten("hymn") == "hymn"