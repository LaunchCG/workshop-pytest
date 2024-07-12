import time
from behave import *
from selenium import webdriver

@given('open browser')
def step_impl(context):
    context.browser = webdriver.Chrome()


@when('Provide application URL')
def step_impl(context):
    context.browser.get('https://opensource-demo.orangehrmlive.com')
    time.sleep(2)


@then('Verify page title')
def step_impl(context):
    act_title = context.browser.title
    exp_title = "OrangeHRM"
    if act_title == exp_title:
        print("Login Test Passed")
    else:
        print("Login Test Failed")
    context.browser.close()

