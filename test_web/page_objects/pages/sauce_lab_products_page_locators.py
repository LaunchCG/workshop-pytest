from selenium.webdriver.common.by import By

class SauceLabsProductsPageLocators(object):
    PRODUCTS_LABEL = (By.XPATH,'//*[@id="header_container"]/div[2]/span')
    ADDTOCART_BOLTTSHIRT_BUTTON = (By.ID,'add-to-cart-sauce-labs-bolt-t-shirt')
    CART_LINK = (By.ID,'shopping_cart_container')


