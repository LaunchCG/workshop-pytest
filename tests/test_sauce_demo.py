from selenium import webdriver
from page_objects.pages.sauce_lab_login_page import SauceLabsLoginPage


def test_sauce_demo(browser):
    
# Commented out code because we're using fixures in order to not repeat code
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # browser.set_page_load_timeout(5000)
    # browser.get("https://www.saucedemo.com/")
    sauce_demo_page = SauceLabsLoginPage(browser)
    sauce_demo_page.enter_username('locked_out_user')
    sauce_demo_page.enter_password('secret_sauce')
    sauce_demo_page.click_login_button()
    
    # Assert on the error text message
    assert sauce_demo_page.text_is_on_page('Sorry, this user has been locked out.') is True
    
    
def test_sauce_cart(browser):
    
 # Commented out code because we're using fixures in order to not repeat code
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # browser.set_page_load_timeout(5000)
    # browser.get("https://www.saucedemo.com/")
    sauce_demo_page = SauceLabsLoginPage(browser)
    sauce_demo_page.enter_username('standard_user')
    sauce_demo_page.enter_password('secret_sauce')
    sauce_demo_page.click_login_button()