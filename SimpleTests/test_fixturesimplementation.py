import pytest


@pytest.fixture
def setup():
    print("Launch browser")
    print("Login")
    print("Browse products")
    yield
    print("checkout")
    print("Logout")

@pytest.fixture
def teardown():
    print("checkout")
    print("Logout")



def testaddtocart(setup):
    print("Add to cart successful")


def testteardowncode(teardown):
    print("teardown check")
