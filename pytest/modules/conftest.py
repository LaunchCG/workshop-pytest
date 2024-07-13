import pytest


@pytest.fixture()
def setup():
    print("Launching Browser")
    print("Open Application")
    yield
    print("Close browser")