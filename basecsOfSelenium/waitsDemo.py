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
driver.delete_cookie("deleted cookies")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(1)
prodResults = driver.find_elements(By.CLASS_NAME,"products .product")

count = len(prodResults)
print(count)
assert count >= 0

for prodResult in prodResults:

    prodResult.find_element(By.CSS_SELECTOR,"div button").click()

print("all the add to card items got selected")
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//*[text()='PROCEED TO CHECKOUT']").click()

#### Sum validation
Sum = 0
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
for price in prices:
    Sum = Sum + int(price.text)

print(Sum)
totalAmount = driver.find_element(By.CSS_SELECTOR,".totAmt").text
assert Sum == int(totalAmount)



driver.find_element(By.CLASS_NAME,"promoCode").send_keys("Rahulshetty")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"promoBtn").click()

##explicit wait
#couponMsg = driver.find_element(By.CLASS_NAME,"promoInfo")
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

