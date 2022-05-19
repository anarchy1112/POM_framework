from locators.locators import HomePageLoc, CheckoutLoc
from pages.basePage import BasePage


class CheckoutPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    def fillFirstCheckoutInfo(self):
        self.click(HomePageLoc.cartBtn)
        self.click(CheckoutLoc.checkoutBtn)


    def fillRestCheckoutInfo(self):
        self.click(CheckoutLoc.adressProceedBtn)
        self.click(CheckoutLoc.shippingChkBx)
        self.click(CheckoutLoc.shippingProceedBtn)
        self.click(CheckoutLoc.paymentMethodBankBtn)
        self.click(CheckoutLoc.confirnOrderBtn)

