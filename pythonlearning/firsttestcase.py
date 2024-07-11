from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Use a raw string or double backslashes for the path
chromedriver_path = r"D:\Python\drivers\chrome-win64\chrome-win64\chromedriver"

# Specify the path to the WebDriver executable
service = Service(executable_path=chromedriver_path)

# Initialize the WebDriver with the Service object
driver = webdriver.Chrome(service)

# Your test case code here

