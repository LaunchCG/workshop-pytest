import pytest


@pytest.mark.usefixtures("setup")
class TestFixtureDemo:

    def test_fixtureDemo(self):
        print("i will be execute steps in fixturesDemo method")

    def test_fixtureDemo1(self):
        print("i will be execute steps in fixturesDemo1 method")

    def test_fixtureDemo2(self):
        print("i will be execute steps in fixturesDemo2 method")

    def test_fixtureDemo3(self):
        print("i will be execute steps in fixturesDemo3 method")