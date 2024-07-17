import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#service_obj = Service("C:\Users\RameshKaramthot\Downloads\chromedriver-win64\chromedriver-win64")
#driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_cookie("deleted cookies")

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)

driver.find_element(By.NAME, "email").send_keys("Ramesh")
driver.find_element(By.XPATH, "//*[@id = 'exampleInputPassword1']").send_keys("Ramesh2805")
driver.find_element(By.CSS_SELECTOR, "*[name = 'name']").send_keys("47928u34")

# protTitle = driver.find_element(By.XPATH, "//*[text()='ProtoCommerce']").text
# print(protTitle)
# assert "Proto" in protTitle

ele = driver.find_element(By.ID, "exampleFormControlSelect1")
dropdown = Select(ele)
dropdown.select_by_index(0)
time.sleep(2)

