
import pytest
from locators.locators import HomePageLoc, CheckoutLoc
from pages.basePage import BasePage
from pages.homePage import HomePage
from tests.baseTest import BaseTest
from pages.checkoutPage import CheckoutPage
from utilities import dataGetter

class TestBuying(BaseTest):

    def test_addToCart(self):
        page=HomePage(self.driver)
        page.addProd1ToCart()
        assert page.textExtraction(HomePageLoc.noOfCartProd)=="1"
        page.screenshot()

    @pytest.mark.parametrize("email,passw", dataGetter.dataGetter("Sheet2"))
    def test_checkout(self,email,passw):
        page=HomePage(self.driver)
        page1=CheckoutPage(self.driver)
        page.fillLoginCreds(email, passw)
        page.goToHomePage()
        page.addProd1ToCart()
        page1.fillFirstCheckoutInfo()
        page1.fillRestCheckoutInfo()
        assert page1.textExtraction(CheckoutLoc.orderConfirmationmsg)=="Your order on My Store is complete."
        page.screenshot()


