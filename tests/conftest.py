from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from locators.locators import BasicInfo


@pytest.fixture(scope="function")
def setUp(request):
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver=driver
    driver.get(BasicInfo.URL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()



