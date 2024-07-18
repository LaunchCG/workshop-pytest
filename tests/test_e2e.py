import time
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Testone(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutPage = homepage.shopItem()
        #self.driver.find_element(By.XPATH, "//*[contains(text(),'Shop')]").click()
        time.sleep(3)

        cards = checkoutPage.get_cardTitles()
        log.info("getting all the card items")
        #products = self.driver.find_elements(By.XPATH, "//*[@class = 'card h-100']")

        i = -1
        for card in cards:
            i = i+1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.addCardButton()[i].click()

        confirmPage = checkoutPage.checkOutBtn()
        #self.driver.find_element(By.XPATH, "//a[contains(@class,'btn-primary')]").click()
        time.sleep(3)
        #confirmPage = ConfirmPage(self.driver)
        confirmPage.getContinueShoppingCheckoutBtn().click()


        #self.driver.find_element(By.CLASS_NAME, "btn-success").click()
        log.info("Entering country name as India")
        confirmPage.getDeliveryLocTxtField("India")

        #self.driver.find_element(By.ID, "country").send_keys("Ind")

        self.webDriverWaitforLinkText("India", 15)
        # wait = WebDriverWait(self.driver, 15)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        confirmPage.autoSuggestDDlLink().click()
        #self.driver.find_element(By.LINK_TEXT, "India").click()

        confirmPage.getPurchaseBtn().click()
        #self.driver.find_element(By.XPATH, "//*[contains(@class,'btn-success')]").click()
        time.sleep(2)
        textMatch = confirmPage.getsuccessAlertMsg().text
        log.info("Text received from application is: "+textMatch)
        assert "Success! Thank you!" in textMatch

        time.sleep(2)


