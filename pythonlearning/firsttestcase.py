 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Use a raw string or double backslashes for the path
chromedriver_path = r"C:\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Specify the path to the WebDriver executable
service = Service(executable_path=chromedriver_path)

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element_by_name()





