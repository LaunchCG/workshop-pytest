import time

from selenium import webdriver

#service_obj = Service("C:\Users\RameshKaramthot\Downloads\chromedriver-win64\chromedriver-win64")
#driver = webdriver.Chrome(service=service_obj)

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("headless")
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(options=chromeOptions)
driver.implicitly_wait(15)
driver.delete_cookie("delete cookies")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)
time.sleep(2)