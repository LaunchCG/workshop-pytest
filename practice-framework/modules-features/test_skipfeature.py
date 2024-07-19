import pytest


class TestClass:
    def test_loginbyemail(self):
        print("this is login by email")
        assert 1 == 1

    @pytest.mark.skip
    def test_loginbyfacebook(self):
        print("this is login by facebook")
        assert 1 == 1

    def test_loginbytwitter(self):
        print("this is login by twitter")
        assert 1 == 1

    @pytest.mark.skip
    def test_signupbyemail(self):
        print("this is signup by email")
        assert 1 == 1

    def test_signupbyfacebook(self):
        print("this is signup by facebook")
        assert 1 == 1

    def test_signupbytwitter(self):
        print("this is signup by twitter")
        assert 1 == 1
