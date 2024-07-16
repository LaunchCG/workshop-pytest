import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestParametrize:
    @pytest.mark.parametrize("username,password", [('Admin', 'admin123'), ('ad', 'admin'), ('admin', 'admin')])
    def test_parametrize(self, username, password):
        self.driver = webdriver.Edge()
        # self.driver.maximize_window()

        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(2)

        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

        time.sleep(2)
        try:
            status = self.driver.find_element(By.XPATH,
                                              '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span').is_displayed()
            self.driver.close()
            assert status is True

        except:
            self.driver.close()
            assert False
