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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action =ActionChains(driver)
element = driver.find_element(By.CSS_SELECTOR,"")
targetElement = driver.find_element(By.CSS_SELECTOR,"")
sourceElement = driver.find_element(By.CSS_SELECTOR,"")

action.context_click(element).perform()
action.click_and_hold(element).perform()
action.drag_and_drop(sourceElement, targetElement).perform()
action.move_to_element(element).perform()


