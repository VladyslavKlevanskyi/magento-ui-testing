from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from data.urls import BASE_URL
from pages.locator import common_locators as comm_locators


class BasePage:
    """
    A base page class that provides common web page interaction methods.
    This class should be inherited by specific page classes.
    """

    def __init__(self, driver: WebDriver):
        """
        Initializes the base page with a WebDriver instance.

        :param driver: WebDriver instance controlling the browser
        """
        self.base_url = BASE_URL
        self.page_url = None
        self.driver = driver

    def open_page(self) -> None:
        """
        Opens the web page by navigating to the full URL.
        Raises an error if page_url is not set.
        """
        if self.page_url:
            self.driver.get(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError(
                "Page can not be opened for this page class"
            )

    def find(self, locator: tuple, element: WebElement = None) -> WebElement:
        """
        Finds a single web element using the provided locator.

        :param locator: Tuple containing locator strategy and locator value
        :param element: Parent element to search within (optional)
        :return: WebElement instance
        """
        if element is None:
            return self.driver.find_element(*locator)
        return element.find_element(*locator)

    def find_all(
            self, locator: tuple, element: WebElement = None
    ) -> list[WebElement]:
        """
        Finds multiple web elements using the provided locator.

        :param locator: Tuple containing locator strategy and locator value
        :param element: Parent element to search within (optional)
        :return: List of WebElement instances
        """
        if element is None:
            return self.driver.find_elements(*locator)
        return element.find_elements(*locator)

    def check_title_is(self, text: str) -> None:
        """
        Asserts that the current page title matches the expected text.

        :param text: Expected title text
        """
        assert self.driver.title == text

    def check_h1_is(self, text: str) -> None:
        """
        Asserts that the main heading (h1) of the page matches the
        expected text.

        :param text: Expected h1 text
        """
        h1 = self.find(comm_locators.tag_h1)
        assert h1.text == text

    def click_logo(self) -> None:
        """
        Clicks on the website's logo element.
        """
        self.find(comm_locators.logo).click()

    def check_if_the_search_field_will_find_existing_product(
            self, product_name: str
    ) -> None:
        """
        Searches for an existing product and verifies that it appears in
        the results.
        Raises an assertion error if the product is not found.

        :param product_name: Name of the product to search for
        """
        # Locate the search field using the locator from common_locators
        search_field = self.find(locator=comm_locators.search_field)

        # Fill the search field with the product name to search for it
        search_field.send_keys(product_name)
        search_field.submit()

        # Locate the products that appear in the search results
        products = self.find_all(comm_locators.product_name)

        # Verify that at least one product appears in the results
        if not products:
            assert False, f"Product {product_name} is not found"

        # Verify that the first product in the results contains the
        # expected product name
        assert product_name in products[0].text, (
            f"Searched product name {product_name} "
            f"but found {products[0].text}"
        )

    def check_search_field_will_not_find_nonexistent_product(
            self, product_name: str
    ) -> None:
        """
        Searches for a nonexistent product and verifies that an appropriate
        message is displayed.

        :param product_name: Name of the nonexistent product to search for
        """
        # Locate the search field using the locator from common_locators
        search_field = self.find(locator=comm_locators.search_field)

        # Clear the search field before entering a new search
        search_field.clear()

        # Fill the search field with the nonexistent product name
        search_field.send_keys(product_name)
        search_field.submit()

        # Locate the search result message element
        message = self.find(comm_locators.search_result_message)

        # Verify that the expected message is displayed
        assert message.text == "Your search returned no results."

    def click_create_an_account_button(self) -> None:
        """
        Clicks the 'Create an Account' button on the page.
        """
        create_account_button = self.find(
            locator=comm_locators.registration_button
        )
        create_account_button.click()
