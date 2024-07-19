import pytest


class TestClass:
    @pytest.mark.sanity
    def test_loginbyemail(self):
        print("this is login by email")
        assert 1 == 1

    @pytest.mark.sanity
    def test_loginbyfacebook(self):
        print("this is login by facebook")
        assert 1 == 1

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginbytwitter(self):
        print("this is login by twitter")
        assert 1 == 1

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_signupbyemail(self):
        print("this is signup by email")
        assert True == True

    @pytest.mark.regression
    def test_signupbyfacebook(self):
        print("this is signup by facebook")
        assert True == True

    @pytest.mark.regression
    def test_signupbytwitter(self):
        print("this is signup by twitter")
        assert True == True
