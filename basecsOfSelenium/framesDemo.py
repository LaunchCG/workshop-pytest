import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#service_obj = Service("C:\Users\RameshKaramthot\Downloads\chromedriver-win64\chromedriver-win64")
#driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.delete_cookie("deleted cookies")
driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(3)

driver.switch_to.frame("mce_0_ifr")
time.sleep(3)
driver.switch_to.default_content()
# driver.find_element(By.ID,"tinymce").clear()
# driver.find_element(By.ID,"tinymce").send_keys("able to automate frames")
