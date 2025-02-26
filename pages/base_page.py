from selenium.webdriver.remote.webdriver import WebDriver
from data.urls import BASE_URL
from pages.locator import common_locators as comm_locators


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
        h1 = self.find(comm_locators.tag_h1)
        assert h1.text == text

    def check_logo_clickability(self):
        self.find(comm_locators.logo).click()
        assert self.driver.title == "Home Page"

    def check_if_the_search_field_will_find_existing_product(
            self, product_name: str
    ):
        search_field = self.find(locator=comm_locators.search_field)
        search_field.send_keys(product_name)
        search_field.submit()
        products = self.find_all(comm_locators.product_name)
        if not products:
            assert False, f"Product {product_name} is not found"
        assert product_name in products[0].text, (
            f"Searched product name {product_name} "
            f"but found {products[0].text}"
        )

    def check_search_field_will_not_find_nonexistent_product(
            self, product_name: str
    ):
        search_field = self.find(locator=comm_locators.search_field)
        search_field.clear()
        search_field.send_keys(product_name)
        search_field.submit()
        message = self.find(comm_locators.search_result_message)
        assert message.text == "Your search returned no results."

    def check_create_an_account_button_functionality(self):
        create_account_button = self.find(
            locator=comm_locators.registration_button
        )
        create_account_button.click()
        assert self.driver.title == "Create New Customer Account"
