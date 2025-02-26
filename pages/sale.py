from data.urls import SALE_URL
from pages.base_page import BasePage
from pages.locator import common_locators as comm_locators


class Sale(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = SALE_URL

    # def check_logo_clickability(self):
    #     self.find(comm_locators.logo).click()
    #     assert self.driver.title == "Home Page"
