import pytest
class TestClass:
    @pytest.fixture() # decorator
    def setup(self):
        print("launching browser...")
        print("Open application.")          #executes once before each test method
        yield
        print("close browser")              #executes once after each test method

    def test_Login(self, setup):
        print("this is login test")

    def test_Search(self,setup):
        print("this is search test")

    def test_Advancedsearch(self,setup):
        print("this is advanced search test")