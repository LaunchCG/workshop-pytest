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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys("pythontest")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertMsg = alert.text
time.sleep(2)
print(alertMsg)
alert.accept()

driver.find_element(By.ID,"confirmbtn").click()
confirmAlertMsg = alert.text
time.sleep(2)
print(confirmAlertMsg)
alert.dismiss()
driver.find_element(By.ID,"confirmbtn").click()
time.sleep(2)
alert.dismiss()



