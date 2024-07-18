import pytest
class TestClass:
    @pytest.fixture() # decorator
    def setup(self):
        print("launching browser...")
        print("Open application.")

    def test_Login(self):
        print("this is login test")

    def test_Search(self,setup):
        print("this is search test")

    def test_Advancedsearch(self,setup):
        print("this is advanced search test")