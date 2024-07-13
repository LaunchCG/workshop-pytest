import pytest
class TestClass:
    @pytest.fixture()
    def setup(self):
        print("Launching Browser")
        print("Open Application")
        yield
        print("Closing Browser")
    def test_Login(self,setup):
        print('this is login test')
    def test_Search(self,setup):
        print('this is search test')
    def test_AdvSearch(self,setup):
        print('this is adv search test')