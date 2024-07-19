import pytest


@pytest.fixture()
def tc_setup():
    print("Launch browser")
    print("Login")
    print("Browse products")
    yield
    print("checkout")
    print("Logout")


@pytest.fixture()
def tc_teardown():
    print("checkout")
    print("Logout")

@pytest.mark.plainfix
def testaddtocart(tc_setup):         #need to pass the fixture method as an argument to the Test
    print("Add to cart successful")

@pytest.mark.plainfix
def testteardowncode(tc_teardown):
    print("teardown check")