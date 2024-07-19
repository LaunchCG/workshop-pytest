import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def test_login_chrome(self):
        from selenium.webdriver.chrome.service import Service
        self.serv_obj = Service("C:\\Users\\DKarmakar\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        time.sleep(3)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        time.sleep(4)
        self.driver.quit()

    # def test_login_edge(self):
    #     from selenium.webdriver.edge.service import Service
    #     self.serv_obj = Service("c:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
    #     self.driver = webdriver.Edge(service=self.serv_obj)
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/")
    #     self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    #     self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    #     self.driver.find_element(By.NAME, "Submit").click()  # Signin
    #     assert self.driver.title == "OrangeHRM"
    #     self.driver.quit()
    #
    # def test_login_firefox(self):
    #     from selenium.webdriver.firefox.service import Service
    #     self.serv_obj = Service("C:\\Drivers\\geckodriver_win64\\geckodriver.exe")
    #     self.driver = webdriver.Firefox(service=self.serv_obj)
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/")
    #     self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    #     self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    #     self.driver.find_element(By.NAME, "Submit").click()  # Signin
    #     assert self.driver.title == "OrangeHRM"
    #     self.driver.quit()
