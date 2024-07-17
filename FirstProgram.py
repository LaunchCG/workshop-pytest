import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5


def test_answer2():
    assert func(6) == 7


def test_answer3():
    assert func(8) == 9