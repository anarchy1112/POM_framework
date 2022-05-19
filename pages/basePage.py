import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



class BasePage:

    def __init__(self, driver):
        self.driver=driver


    def click(self,locator):
        self.driver.find_element(By.XPATH,locator).click()

    def type(self,locator,text):
        self.driver.find_element(By.XPATH,locator).send_keys(text)

    def clear(self,locator):
        self.driver.find_element(By.XPATH,locator).clear

    def wait(self,locator):
        # element=self.driver.find_element(By.XPATH,locator)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,locator)))

    def mouseOver(self,locator):
        elem=self.driver.find_element(By.XPATH,locator)
        action=ActionChains(self.driver)
        action.move_to_element(elem).perform()

    def textExtraction(self,locator):
        return self.driver.find_element(By.XPATH,locator).text

    def dropdown(self,locator, value):
        drop=self.driver.find_element(By.XPATH, locator)
        select=Select(drop)
        select.select_by_value(value)

    def screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(),name="screenshot",attachment_type=AttachmentType.PNG)

