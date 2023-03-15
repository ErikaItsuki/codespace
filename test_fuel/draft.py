import pytest

def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)

def main():
    try:
        main()
    except RuntimeError:
        test_recursion_depth()

main()