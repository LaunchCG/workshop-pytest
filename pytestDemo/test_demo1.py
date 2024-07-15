import pytest

@pytest.mark.xfail
def test_first():
    a = 1
    b = 2
    assert a == b
    print("testing using pytest framework")



@pytest.mark.skip
def test_second():
    print("Good morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])