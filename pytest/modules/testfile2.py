import pytest



def func(x):
    return x + 1


@pytest.mark.xfail
def test_answer():
    assert func(3) == 2


@pytest.mark.skip
def test_answer1():
    assert func(5) == 6


def test_answer2():
    assert func(6) == 7
