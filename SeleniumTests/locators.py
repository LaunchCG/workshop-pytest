import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# xpath syntax - //tagname[@attribute='value']
# css selector syntax - tagname[attribute='value']
# xpath based on text in the page - //tagname[text()='text_value']
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Siva")
driver.find_element(By.NAME, "email").send_keys("siva@abc.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
time.sleep(2)

#Dropdown Selection
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)
msg = driver.find_element(By.CLASS_NAME, "alert-success").text
print(msg)
assert "Success!" in msg
driver.close()



