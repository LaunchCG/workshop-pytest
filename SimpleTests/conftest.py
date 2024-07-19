import pytest


@pytest.fixture(scope = "session", autouse=True)
def tc_setup():
    print("Launch browser")
    print("Login")
    print("Browse products")
    yield
    print("checkout")
    print("Logout")


# @pytest.fixture(autouse=True)
# def tc_teardown():
#     print("checkout")
#     print("Logout")