from selenium.webdriver.remote.webdriver import WebDriver
from data.urls import BASE_URL
from pages.locator import common_locators as locators


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

    def find(self, locator: tuple, element: WebDriver = None):
        if element is None:
            return self.driver.find_element(*locator)
        return element.find_element(*locator)

    def find_all(self, locator: tuple, element: WebDriver = None):
        if element is None:
            return self.driver.find_elements(*locator)
        return element.find_elements(*locator)

    def check_title_is(self, text):
        assert self.driver.title == text

    def check_h1_is(self, text):
        h1 = self.find(locators.tag_h1)
        assert h1.text == text
