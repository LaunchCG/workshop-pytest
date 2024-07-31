import time
from selenium import webdriver
from test_web.page_objects.pages.sauce_lab_login_page import SauceLabsLoginPage
from test_web.page_objects.pages.sauce_lab_products_page import SauceLabsProductsPage


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
    sauce_login_page = SauceLabsLoginPage(browser)
    # Enter UserName = "standard_user"
    sauce_login_page.enter_username("standard_user")

    # Enter Password = "secret_sauce"
    sauce_login_page.enter_password("secret_sauce")

    # Click Login button
    sauce_login_page.click_login_button()

    #Access Products Page
    sauce_products_page = SauceLabsProductsPage(browser)

    #Verify Label on Products Page
    assert sauce_products_page.label_is_on_page("Products") is True

    #Click add to cart Sauce Labs Bolt T-Shirt
    sauce_products_page.click_add_to_cart_button()

    #Click on cart link
    sauce_products_page.click_cart_link()
    time.sleep(2)













