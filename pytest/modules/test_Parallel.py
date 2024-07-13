import time
import pytest
from selenium import webdriver


class TestLogin:
    def test_login_chrome(self):
        from selenium.webdriver.common.by import By
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(2)

        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

        time.sleep(2)

        act_title = self.driver.title
        exp_title = "OrangeHRM"
        if act_title == exp_title:
            print("Login Test Passed")
        else:
            print("Login Test Failed")
        self.driver.close()

    def test_login_edge(self):
        from selenium.webdriver.common.by import By
        self.driver = webdriver.Edge
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        time.sleep(2)

        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

        time.sleep(2)

        act_title = self.driver.title
        exp_title = "OrangeHRM"
        if act_title == exp_title:
            print("Login Test Passed")
        else:
            print("Login Test Failed")
        self.driver.close()
