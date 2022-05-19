from selenium.webdriver.common.by import By

from locators.locators import HomePageLoc, SignInPageLoc, RegPageLoc, LoggedInPage

from pages.basePage import BasePage


class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def goToRegistration(self, email):
        self.click(HomePageLoc.signInBtn)
        self.type(SignInPageLoc.regEmail, email)
        self.click(SignInPageLoc.regBtn)


    def fillRegForm(self,firstname, lastname, pasw,company,address1,address2,city,zipcode, additinfo, phoneHome, phoneMobile, aliasAddress):
        self.click(RegPageLoc.mrRadio)
        self.type(RegPageLoc.firstName,firstname)
        self.type(RegPageLoc.lastName,lastname)
        self.type(RegPageLoc.passw, pasw)
        self.dropdown(RegPageLoc.dayDropd,"1")
        self.dropdown(RegPageLoc.monthDropd, "10")
        self.dropdown(RegPageLoc.yearDropd,"1980")
        self.type(RegPageLoc.compName,company)
        self.type(RegPageLoc.address1,address1)
        self.type(RegPageLoc.address2, address2)
        self.type(RegPageLoc.city,city)
        self.dropdown(RegPageLoc.stateDropd,'1')
        self.type(RegPageLoc.postcode,zipcode)
        # self.dropdown(RegPageLoc.countryDropd,"United States")
        self.type(RegPageLoc.additInfo, additinfo)
        self.type(RegPageLoc.phoneHome,phoneHome)
        self.type(RegPageLoc.phoneMobile,phoneMobile)
        self.clear(RegPageLoc.aliasAddress)
        self.type(RegPageLoc.aliasAddress, aliasAddress)
        self.click(RegPageLoc.registBtn)
        self.wait(LoggedInPage.signOutBtn)

    def fillLoginCreds(self,email,passw):
        self.click(HomePageLoc.signInBtn)
        self.type(SignInPageLoc.signInEmail, email)
        self.type(SignInPageLoc.signInPass, passw)
        self.click(SignInPageLoc.signInBtn)

    def addProd1ToCart(self):
        self.mouseOver(HomePageLoc.prod1)
        self.click(HomePageLoc.prod1AddCart)
        self.click(HomePageLoc.popUpClose)

    def goToCart(self):
        self.click(HomePageLoc.cartBtn)

    def goToHomePage(self):
        self.click(HomePageLoc.homePageBtn)
