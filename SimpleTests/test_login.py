import pytest


class TestClass:
    def testlogin(self):
        print("Login successful !!")

    def testlogoff(self):
        print("Logoff successful !!")

    @pytest.mark.smoke
    def testcalculation(self):
        assert 2+3 == 5


