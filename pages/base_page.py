from selenium.webdriver.remote.webdriver import WebDriver
from data import BASE_URL


class BasePage:

    def __init__(self, driver: WebDriver):
        self.base_url = BASE_URL
        self.page_url = None
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError(
                "Page can not be opened for this page class"
            )

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)
