import time
import pytest
from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is: "+getData["firstname"])

        self.waitforElement(homepage.name, 15)
        homepage.get_name().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPassword().send_keys(getData["password"])
        time.sleep(2)

        self.selectDropDownByText(homepage.getGenderDdl(), getData["gender"])
        #homepage.getGender().send_keys(getData["gender"])
        homepage.get_form_submit_btn().click()
        assert "Success!" in homepage.get_form_submission_success_msg().text, "success alert message is not populated"
        time.sleep(3)
        self.driver.refresh()

    #@pytest.fixture(params=HomePageData.getTestData("testcase3"))     ## driving data from excelsheet
    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getData(self, request):
        return request.param







        #self.driver.find_element(By.NAME, "email").send_keys("Ramesh")
        #driver.find_element(By.XPATH, "//*[@id = 'exampleInputPassword1']").send_keys("Ramesh2805")
        #driver.find_element(By.CSS_SELECTOR, "*[name = 'name']").send_keys("47928u34")
        # protTitle = driver.find_element(By.XPATH, "//*[text()='ProtoCommerce']").text
        # print(protTitle)
        # assert "Proto" in protTitle


