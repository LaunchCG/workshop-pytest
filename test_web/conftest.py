import pytest
from pytest_metadata.plugin import metadata_key
from selenium.webdriver import Chrome
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.set_page_load_timeout(5000)

    env_url = 'https://www.saucedemo.com'
    driver.get(env_url)

    yield driver

    driver.quit()
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Pytest workshop"
    config.stash[metadata_key]["Module Name"] = "WebTesting with Pytest"
    config.stash[metadata_key]["Tester Name"] = "Pradeep Edara"

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Python", None)
