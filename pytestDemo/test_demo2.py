import pytest

@pytest.mark.smoke
def test_first(setup):
    msg = "Hello"
    assert msg == "Hello", "test is failed because strings doesn't match"

@pytest.mark.regression
def test_sec_program():
    a = 4
    b = 6
    assert a+2 == b, "additional not matched"