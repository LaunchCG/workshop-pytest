import pytest


@pytest.mark.usefixtures("tc_setupNew")
class TestFixtureExamples:
    @pytest.mark.fixtureTesting
    def testaddtocart1(self):
        print("Add to cart successful")

    @pytest.mark.fixtureTesting
    def testteardowncode1(self):
        print("teardown check")



