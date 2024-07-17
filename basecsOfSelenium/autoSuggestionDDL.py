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

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR,"*[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        break


print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"
#assert "India" in resCountry
time.sleep(3)

