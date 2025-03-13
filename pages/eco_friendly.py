import random

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import ECO_FRIENDLY_URL
from pages.base_page import BasePage
from pages.locator import common_locators as comm_locators


class CollectionsEcoFriendly(BasePage):
    """
    A page class that represents the eco-friendly product collection page.
    Inherits from BasePage and provides specific methods to interact with
    the eco-friendly product collection page.
    """
    def __init__(self, driver):
        """
        Initializes the CollectionsEcoFriendly page with a WebDriver instance.

        :param driver: WebDriver instance controlling the browser
        """
        super().__init__(driver)
        self.page_url = ECO_FRIENDLY_URL

    def check_number_of_products_is(self, number: int) -> None:
        """
        Asserts that the number of products displayed on the page is less than
        or equal to the specified number.

        :param number: Maximum expected number of products
        """
        all_products = self.find_all(comm_locators.product)
        assert len(all_products) <= number, (
            f"Expected number of products less than or equal to {number}, "
            f"but found {len(all_products)}"
        )

    def add_product_to_cart(self) -> None:
        """
        Adds a product to the cart by selecting size, color, and clicking
        the 'Add to Cart' button.

        Performs the action using ActionChains to simulate hover and clicks.
        """
        # Locate the first product
        product = self.find(comm_locators.product)

        # Locate available size and color options for the product
        size_list = self.find_all(
            element=product,
            locator=comm_locators.size_element
        )
        color_list = self.find_all(
            element=product,
            locator=comm_locators.color_element
        )

        # Locate the 'Add to Cart' button
        add_to_cart_button = self.find(comm_locators.add_to_cart_button)

        # Use ActionChains to simulate mouse actions
        actions = ActionChains(self.driver)
        actions.move_to_element(product)
        actions.move_to_element(size_list[0])
        actions.click()
        actions.move_to_element(color_list[0])
        actions.click()
        actions.move_to_element(add_to_cart_button)
        actions.click()
        actions.perform()

    def check_number_of_products_in_cart_is(self, number: int) -> None:
        """
         Asserts that the number of products in the cart matches the expected
         number.

         :param number: Expected number of products in the cart
         """
        # Locate the cart product counter and wait until the counter
        # has a non-empty value
        element = self.find(comm_locators.counter_number)
        WebDriverWait(self.driver, 2).until(
            lambda d: element.text.strip() != ""
        )

        # Verify that the cart counter matches the expected number
        counter_number = self.find(comm_locators.counter_number)
        assert counter_number.text == str(number), (
            f"Expected {number} products in the cart, but "
            f"found {counter_number.text}"
        )

    def go_to_product_page(self) -> None:
        """
        Clicks on a randomly selected product from the product list and
        asserts that the product's page loads correctly by checking the
        page's h1 title matches the product's name.

        Verifies navigation to the selected product's page.
        """
        # Get all the products and select one at random
        all_products = self.find_all(comm_locators.product)
        random_product = all_products[
            random.randint(0, len(all_products) - 1)
        ]

        # Get the product name and click the product to go to its page
        product_name = self.find(
            element=random_product,
            locator=comm_locators.product_name
        ).text
        random_product.click()

        # Verify that the h1 element on the product page matches the
        # product's name
        h1_text = self.find(comm_locators.tag_h1)
        assert h1_text.text == product_name
