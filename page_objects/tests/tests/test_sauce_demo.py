import pytest
from dns.query import https
from selenium import webdriver
from page_objects.pages.sauce_labs_login_page import SauceLabsLoginPage


def test_sauce_demo():
    browser = webdriver.Chrome

    browser.maximize_window()
    browser.set_page_load_timeout(5000)

    browser.get('https: // www.saucedemo.com/')

    sauce_demo_page = SauceLabsLoginPage(browser)
    sauce_demo_page.enter_username('locked_out_user')
