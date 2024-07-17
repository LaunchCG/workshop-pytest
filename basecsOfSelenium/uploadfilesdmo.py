import time

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_upload():

    fruit_name = "Apple"
    file_path = "C:\\Users\\RameshKaramthot\\Downloads\\download.xlsx"
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/upload-download-test/")
    time.sleep(3)
    driver.find_element(By.ID, "downloadButton").click()
    time.sleep(3)

    book = openpyxl.load_workbook(file_path)
    sheet = book.active
    sheet.cell(row=5, column=4).value = "1300"


    file_input = driver.find_element(By.ID,"fileinput")
    file_input.send_keys(file_path)

    time.sleep(3)
    price_column = driver.find_element(By.XPATH, "//div[text()='Price']").get_attribute("data-column-id")
    print(price_column)
    time.sleep(3)
    apple_price = driver.find_element(By.ID,"//*[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+price_column+"price_column-undefined']").text
    print(apple_price)