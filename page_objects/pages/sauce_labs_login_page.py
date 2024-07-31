from page_objects.pages import Basepage
from page_objects.pages.sauce_labs_login_page_locators import SauceLabsLoginPageLocators
from selenium.webdriver.support import expected_conditions as EC

class SauceLabsLoginPage(Basepage):
    def enter_username(self, username: str):
        element = self.wait.until(EC.presence_of_element_located(SauceLabsLoginPageLocators.USERNAME_FIELD))
        element.send_keys(username)

    def enter_password(self, password: str):
        element = self.wait.until(EC.presence_of_element_located(SauceLabsLoginPageLocators.PASSWORD_FIELD))
        element.send_keys(password)

    def click_login_button(self):
        element = self.wait.until(EC.presence_of_element_located(SauceLabsLoginPageLocators.LOGIN_BUTTON))
        element.click()



