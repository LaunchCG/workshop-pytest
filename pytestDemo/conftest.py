import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be execute first")
    yield
    print("i will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile data being created")
    return ["Python", "pytest", "fixtures"]


@pytest.fixture(params=[("chrome", "Python", "testing"), ("firefox", "fixturesss"), "IE"])
def crossBrowser(request):
    return request.param

