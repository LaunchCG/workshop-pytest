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

checkboxes = driver.find_elements(By.CSS_SELECTOR,"*[type = 'checkbox']")
print(len(checkboxes))
time.sleep(3)
for checkbox in checkboxes:
    #checkbox.text == "Option1"
    if checkbox.get_attribute("value") == "option2":
        time.sleep(1)
        checkbox.click()
        assert checkbox.is_selected()
        break



radioBtns = driver.find_elements(By.CSS_SELECTOR,"*[type='radio']")
print(len(radioBtns))
radioBtns[2].click()
assert radioBtns[2].is_selected()

# for radioBtn in radioBtns:
#     if radioBtn.get_attribute("value") == "radio2":
#         radioBtn.click()
#         time.sleep(2)
