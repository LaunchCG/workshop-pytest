import pytest


class TestClass:
    @pytest.mark.smoke
    def testlogin(self):
        print("Login successful !!")

    def testlogoff(self):
        print("Logoff successful !!")

    @pytest.mark.skip
    def testcalculation(self):
        assert 2+3 == 5


