from test_web.page_objects.pages import BasePage
from test_web.page_objects.pages.sauce_lab_products_page_locators import SauceLabsProductsPageLocators
from selenium.webdriver.support import expected_conditions as EC


class SauceLabsProductsPage(BasePage):
    def click_add_to_cart_button(self):
        element = self.wait.until(EC.presence_of_element_located(SauceLabsProductsPageLocators.ADDTOCART_BOLTTSHIRT_BUTTON))
        element.click()

    def label_is_on_page(self, message: str):
        return message in self.wait.until(EC.presence_of_element_located(SauceLabsProductsPageLocators.PRODUCTS_LABEL)).text
    def click_cart_link(self):
        element = self.wait.until(EC.presence_of_element_located(SauceLabsProductsPageLocators.CART_LINK))
        element.click()

