import pytest

@pytest.mark.skip
def test_greater():
    num = 50
    assert num < 5
@pytest.mark.hello
def test_greater_equal():
    num = 100
    assert num >= 50