from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SauceLabsLoginPageLocators(object):
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    BODY = (By.TAG_NAME, 'body')