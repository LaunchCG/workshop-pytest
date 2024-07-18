
def func(x):
    return x % 2


def test_divisibleby2():
    assert func(6) == 0


def test_one():
    x = "this"
    assert "i" in x


def test_two():
    x = "hello"
    assert hasattr(x,"check")