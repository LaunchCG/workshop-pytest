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
driver.implicitly_wait(5)
driver.maximize_window()
driver.delete_cookie("delete cookies")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//*[contains(text(),'Shop')]").click()
time.sleep(3)
products = driver.find_elements(By.XPATH,"//*[@class = 'card h-100']")
for product in products:
    prodName = product.find_element(By.XPATH,"div/h4/a").text
    if prodName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()
driver.find_element(By.XPATH,"//a[contains(@class,'btn-primary')]").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME,"btn-success").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait = WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

driver.find_element(By.XPATH,"//*[contains(@class,'btn-success')]").click()
time.sleep(2)
assert "Success! Thank you!" in driver.find_element(By.CLASS_NAME,"alert-success ").text


time.sleep(2)
