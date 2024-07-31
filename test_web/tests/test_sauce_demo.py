import time
from selenium import webdriver
from test_web.page_objects.pages.sauce_lab_login_page import SauceLabsLoginPage


def test_sauce_demo(browser):
    #Enter UserName = "locked_out_user"
    sauce_demo_page = SauceLabsLoginPage(browser)
    sauce_demo_page.enter_username("locked_out_user")

    #Enter Password = "secret_sauce"
    sauce_demo_page.enter_password("secret_sauce")

    #Click Login button
    sauce_demo_page.click_login_button()

    #Verify "locked out " message appears
    assert sauce_demo_page.text_is_on_page("Sorry, this user has been locked out.") is True


def test_sauce_cart(browser):
    sauce_demo_page = SauceLabsLoginPage(browser)
    sauce_demo_page.enter_username("locked_out_user")

    # Enter Password = "secret_sauce"
    sauce_demo_page.enter_password("secret_sauce")

    # Click Login button
    sauce_demo_page.click_login_button()

    # Verify "locked out " message appears
    assert sauce_demo_page.text_is_on_page("Sorry, this user has been locked out.") is True
