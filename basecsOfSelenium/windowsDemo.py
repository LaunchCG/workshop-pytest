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
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Click Here").click()

allWindows = driver.window_handles
driver.switch_to.window(allWindows[1])
windowTitle = driver.find_element(By.TAG_NAME,"h3").text
print(windowTitle)
assert "New Window" == windowTitle

driver.switch_to.window(allWindows[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text

###### driver.switch_to.default_content()

