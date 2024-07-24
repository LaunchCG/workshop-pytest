import pytest


def func(x):
    return x + 1

@pytest.mark.flaky(reruns=10)
@pytest.mark.this
def test_answer():
    assert func(3) == 5

@pytest.mark.skip
def test_answer2():
    assert func(6) == 7