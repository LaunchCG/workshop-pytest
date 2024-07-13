import pytest
class TestClass:
    @pytest.mark.run(order=5)
    def test_methodE(self):
        print("This is Test Method E...")
        assert True==True

    @pytest.mark.run(order=4)
    def test_methodD(self):
            print("This is Test Method D...")
            assert True == True
    @pytest.mark.run(order=1)
    def test_methodA(self):
        print("This is Test Method A...")
        assert True==True

    @pytest.mark.run(order=3)
    def test_methodC(self):
        print("This is Test Method C...")
        assert True==True

    @pytest.mark.run(order=2)
    def test_methodB(self):
        print("This is Test Method B...")
        assert True == True