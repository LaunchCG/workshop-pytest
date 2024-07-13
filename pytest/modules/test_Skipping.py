import pytest
class TestClass:
    def test_LoginByEmail(self):
        print("This is login by email")
        assert True==True
    @pytest.mark.skip
    def test_LoginByFaceBook(self):
        print("This is login by FaceBook")
        assert True==True
    def test_LoginByTwitter(self):
        print("This is login by Twitter")
        assert True==True
    def test_SignUpByEmail(self):
        print("This is SignUp by email")
        assert True==True

    @pytest.mark.skip
    def test_SignUpByFaceBook(self):
        print("This is SignUp by FaceBook")
        assert True==True
    def test_SignUpByTwitter(self):
        print("This is SignUp by Twitter")
        assert True==True

