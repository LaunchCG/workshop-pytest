import inspect
import logging

import pytest
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def webDriverWaitforLinkText(self, text, timeout):
        self.logger = self.getLogger()
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
            self.logger.info(f"Element with link text '{text}' found.")
        except TimeoutException as t:
            self.logger.error(f"The link text '{text}' was not found within {timeout} seconds. TimeoutException: {t}")
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")

    def waitforElement(self, locator, timeout):
        self.logger = self.getLogger()
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(expected_conditions.presence_of_element_located((locator)))
            self.logger.info(f"Element with locator '{locator}' found.")
        except TimeoutException as t:
            self.logger.error(
                f"Element with locator '{locator}' was not found within {timeout} seconds. TimeoutException: {t}")
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")

    def selectDropDownByIndex(self, locator, index_value):
        try:

            dropdown = Select(locator)
            dropdown.select_by_index(index_value)
        except NoSuchElementException as e:
            print(f"DropDownList index Element not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def selectDropDownByValue(self, locator, ddl_value):
        try:
            dropdown = Select(locator)
            dropdown.select_by_value(ddl_value)
        except NoSuchElementException as e:
            print(f"DDl element value not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def selectDropDownByText(self, locator, ddl_text):
        try:
            self.waitforElement(locator, 15)
            dropdown = Select(locator)
            dropdown.select_by_visible_text(ddl_text)
        except NoSuchElementException as e:
            print(f"DDl Element text not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")



