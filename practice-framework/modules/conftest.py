import pytest
@pytest.fixture()  # decorator
def setup():
    print("launching browser...")
    print("Open application.")  # executes once before each test method
    yield
    print("close browser....")  # executes once after each test method