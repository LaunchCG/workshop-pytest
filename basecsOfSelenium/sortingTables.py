import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#service_obj = Service("C:\Users\RameshKaramthot\Downloads\chromedriver-win64\chromedriver-win64")
#driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.maximize_window()
driver.delete_cookie("deleted cookies")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")


browserSortedVeggies = []
driver.find_element(By.XPATH,"//*[text()='Veg/fruit name']").click()
veggiesWebElementsList = driver.find_elements(By.XPATH,"//tr/td[1]")

for ele in veggiesWebElementsList:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()
browserSortedVeggies.sort()  ### to check whether the list is following sorting technique or not === A,B,C,D
assert browserSortedVeggies == originalBrowserSortedList