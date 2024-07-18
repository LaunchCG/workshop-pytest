from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    continueShoppingCheckoutBtn = (By.CLASS_NAME, "btn-success")
    deliveryLocTxtField = (By.ID, "country")
    autoSuggestDDlResult = (By.LINK_TEXT, "India")
    purchaseBtn = (By.XPATH, "//*[contains(@class,'btn-success')]")
    successAlertMsg = (By.CLASS_NAME, "alert-success ")

    def getContinueShoppingCheckoutBtn(self):
        return self.driver.find_element(*ConfirmPage.continueShoppingCheckoutBtn)

    def getDeliveryLocTxtField(self, text):
        return self.driver.find_element(*ConfirmPage.deliveryLocTxtField).send_keys(text)

    def autoSuggestDDlLink(self):
        return self.driver.find_element(*ConfirmPage.autoSuggestDDlResult)

    def getPurchaseBtn(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    def getsuccessAlertMsg(self):
        return self.driver.find_element(*ConfirmPage.successAlertMsg)