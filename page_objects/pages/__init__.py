import driver
import self
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Basepage(object):

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=30)
