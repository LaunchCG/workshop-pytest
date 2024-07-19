import pytest


def func(x):
    return x % 2

@pytest.mark.smoke
def test_divisibleby2():
    assert func(6) == 0


def test_one():
    x = "this"
    assert "s" in x


def test_two():
    x = "hello"
    assert hasattr(x,"check")


def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])