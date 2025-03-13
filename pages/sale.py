from data.urls import SALE_URL
from pages.base_page import BasePage


class Sale(BasePage):
    """
    A page class that represents the sale page.
    Inherits from BasePage and provides specific methods to interact with
    the sale page.
    """
    def __init__(self, driver):
        """
        Initializes the Sale page with a WebDriver instance.

        :param driver: WebDriver instance controlling the browser
        """
        super().__init__(driver)
        self.page_url = SALE_URL
