# test_login.py

import pytest


class TestLogin:
    def test_loginbyemail(self, setup):
        print("this is login by email")
        assert True == True

    def test_loginbyfacebook(self, setup):
        print("this is login by facebook")
        assert True == True

    def test_loginbytwitter(self, setup):
        print("this is login by twitter")
        assert True == True
