import pytest


@pytest.mark.parametrize("secret_number", [9])
def test_addition(secret_number):
    assert secret_number + 1 == 10


@pytest.mark.parametrize("secret_number", [9])
def test_subtraction(secret_number):
    assert secret_number - 7 == 2


@pytest.mark.parametrize("secret_number", [6])
def test_divide(secret_number):
    assert secret_number / 3 == 2
