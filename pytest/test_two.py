import pytest
class TestClass:
    @pytest.fixture()
    def setup(self):
        print("Launching Browser")
        print("Open Application")
    def test_Login(self,setup):
        print('this is login test')
    def test_Search(self,setup):
        print('this is search test')
    def test_AdvSearch(self):
        print('this is adv search test')