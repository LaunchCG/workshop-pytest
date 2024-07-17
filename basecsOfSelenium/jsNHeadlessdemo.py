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

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.delete_cookie("deleted cookies")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
driver.execute_script("window.scrollBy(0, 500);")
print("page scrolled to y 500")

### screenshot
#driver.get_screenshot_as_file("screen.png")