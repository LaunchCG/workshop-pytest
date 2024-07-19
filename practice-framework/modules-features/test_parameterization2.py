import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestClass:
    @pytest.mark.parametrize('user, pwd', [("Admin", "admin123"), ('rr', 'adm2')])
    def test_login(self, user, pwd):
        self.serv_obj = Service("C:\\Users\\DKarmakar\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        time.sleep(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.NAME, "username").send_keys(user)
        self.driver.find_element(By.NAME, "password").send_keys(pwd)
        self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
        try:
            self.status=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status==True
        except:
            self.driver.close()
            assert False


