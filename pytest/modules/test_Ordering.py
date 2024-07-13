import pytest
class TestClass:
    @pytest.mark.fifth
    def test_methodE(self):
        print("This is Test Method E...")
        assert True==True

    @pytest.mark.fourth
    def test_methodD(self):
            print("This is Test Method D...")
            assert True == True
    @pytest.mark.first
    def test_methodA(self):
        print("This is Test Method A...")
        assert True==True

    @pytest.mark.third
    def test_methodC(self):
        print("This is Test Method C...")
        assert True==True

    @pytest.mark.second
    def test_methodB(self):
        print("This is Test Method B...")
        assert True == True