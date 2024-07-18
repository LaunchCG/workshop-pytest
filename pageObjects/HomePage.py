from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//*[contains(text(),'Shop')]")
    name = (By.NAME,"name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    genderDdl = (By.ID, "exampleFormControlSelect1")
    form_submit_btn = (By.CLASS_NAME,"btn-success")
    form_submission_success_msg = (By.CLASS_NAME, "alert-success")




###   page is navigating to next page checkout page so created object here itself ###

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getGenderDdl(self):
        return self.driver.find_element(*HomePage.genderDdl)

    def get_form_submit_btn(self):
        return self.driver.find_element(*HomePage.form_submit_btn)

    def get_form_submission_success_msg(self):
        return self.driver.find_element(*HomePage.form_submission_success_msg)

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage