from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.CSS_SELECTOR, ".card-title a")
    addCardButtonEle = (By.CSS_SELECTOR, ".card-footer button")
    checkOutBtnEle = (By.XPATH, "//a[contains(@class,'btn-primary')]")


    def get_cardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitles)

    def addCardButton(self):
        return self.driver.find_elements(*CheckoutPage.addCardButtonEle)


###   page is navigating to next page confirm page so created object here itself ###
    def checkOutBtn(self):
        self.driver.find_element(*CheckoutPage.checkOutBtnEle).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage


