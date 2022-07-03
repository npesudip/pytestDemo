# Importing necessary  packages
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.pageTitles import *
from pageObjects.urlLists import *
from pageObjects.locators import *


# Test Class :
class Test_HomePage:

    def setup_method(self, method):
        self.driver = webdriver.Chrome(driver_path)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_001_get_home_page(self):
        self.driver.get(baseurl)
        assert self.driver.title == title_index_page

    def test_002_click_on_about_us_icon(self):
        self.driver.get(baseurl)
        self.driver.find_element(By.XPATH, xpath_about_us_icon).click()
        assert self.driver.title == title_about_us_page
