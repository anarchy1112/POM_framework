import allure
import pytest
from locators.locators import LoggedInPage
from pages.homePage import HomePage
from tests.baseTest import BaseTest
from utilities import dataGetter

class TestRegLog(BaseTest):

    @pytest.mark.parametrize("email,firstname, lastname, pasw,company,address1,address2,city,zipcode, additinfo, phoneHome, phoneMobile, aliasAddress",dataGetter.dataGetter("Sheet1"))
    def test_regist(self, email,  firstname, lastname, pasw, company, address1, address2, city, zipcode, additinfo, phoneHome, phoneMobile, aliasAddress):
        page=HomePage(self.driver)
        page.goToRegistration(email)
        page.fillRegForm(firstname, lastname, pasw,company,address1,address2,city,zipcode, additinfo, phoneHome, phoneMobile, aliasAddress)
        page.screenshot()
        assert page.textExtraction(LoggedInPage.signOutBtn)=='Sign out'


    @pytest.mark.parametrize("email,passw", dataGetter.dataGetter("Sheet2"))
    def test_logIn(self, email,passw):
        page=HomePage(self.driver)
        page.fillLoginCreds(email,passw)
        page.screenshot()
        assert page.textExtraction(LoggedInPage.signOutBtn) == 'Sign out'
