

class BasicInfo:
    URL="http://automationpractice.com/index.php"

class HomePageLoc:
    signInBtn='//*[@id="header"]/div[2]/div/div/nav/div[1]/a'
    contactUsBtn='//*[@id="contact-link"]/a'
    cartBtn='//*[@id="header"]/div[3]/div/div/div[3]/div/a'
    tshirtCat='//*[@id="block_top_menu"]/ul/li[3]/a'
    womanCat='//*[@id="block_top_menu"]/ul/li[1]/a'
    dressesCat='//*[@id="block_top_menu"]/ul/li[2]/a'
    prod1="//li[@class='ajax_block_product col-xs-12 col-sm-4 col-md-3 first-in-line first-item-of-tablet-line first-item-of-mobile-line']//img[@title='Faded Short Sleeve T-shirts']"
    prod1AddCart='//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]/span'
    prod1More='//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[2]/span'
    prod1Price='//*[@id="homefeatured"]/li[1]/div/div[2]/div[1]/span'
    popUpPrice='//*[@id="layer_cart"]/div[1]/div[2]/div[1]/span'
    popUpCheckoutBtn='//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span'
    popUpClose='//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span'
    noOfCartProd='//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[1]'
    homePageBtn='//*[@id="header_logo"]/a/img'

class SignInPageLoc:
    signInEmail='//input[@id="email"]'
    signInPass='//input[@id="passwd"]'
    signInBtn='//span[normalize-space()="Sign in"]'
    regEmail='//input[@id="email_create"]'
    regBtn='//span[normalize-space()="Create an account"]'

class RegPageLoc:
    mrRadio='//input[@id="id_gender1"]'
    mrsRadio='//input[@id="id_gender2"]'
    firstName='//input[@id="customer_firstname"]'
    lastName='//input[@id="customer_lastname"]'
    dayDropd='//select[@id="days"]'
    monthDropd='//select[@id="months"]'
    yearDropd='//select[@id="years"]'
    firstName2='//input[@id="firstname"]'
    lastName2='//input[@id="lastname"]'
    compName='//input[@id="company"]'
    address1='//input[@id="address1"]'
    address2='//input[@id="address2"]'
    city='//input[@id="city"]'
    stateDropd='//select[@id="id_state"]'
    postcode='//input[@id="postcode"]'
    countryDropd='//select[@id="id_country"]'
    additInfo='//textarea[@id="other"]'
    phoneHome='//input[@id="phone"]'
    phoneMobile='//input[@id="phone_mobile"]'
    aliasAddress='//input[@id="alias"]'
    passw='//input[@id="passwd"]'
    newslChkbx='//input[@id="newsletter"]'
    offerChkbx='//input[@id="optin"]'
    textCreate='//*[@id="noSlide"]/h1'
    registBtn='//*[@id="submitAccount"]/span'


class LoggedInPage:
    signOutBtn='//*[@id="header"]/div[2]/div/div/nav/div[2]/a'


class CheckoutLoc:
    unitPrice='//*[@id="total_product_price_1_1_0"]'
    checkoutBtn='//*[@id="center_column"]/p[2]/a[1]/span'
    totalPrice='//*[@id="total_product_price_1_1_0"]'
    adressProceedBtn='//*[@id="center_column"]/form/p/button/span'
    shippingProceedBtn='//*[@id="form"]/p/button/span'
    shippingChkBx='//*[@id="uniform-cgv"]'
    paymentMethodBankBtn='//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a'
    confirnOrderBtn='//*[@id="cart_navigation"]/button/span'
    orderConfirmationmsg='//*[@id="center_column"]/div/p/strong' #Your order on My Store is complete.

