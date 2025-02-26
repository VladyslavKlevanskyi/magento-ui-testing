import random

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import ECO_FRIENDLY_URL
from pages.base_page import BasePage
from pages.locator import common_locators as comm_locators


class CollectionsEcoFriendly(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = ECO_FRIENDLY_URL

    def check_number_of_products_is(self, number):
        all_products = self.find_all(comm_locators.product)
        assert len(all_products) <= number

    def add_product_to_cart(self):
        product = self.find(comm_locators.product)
        size_list = self.find_all(
            element=product,
            locator=comm_locators.size_element
        )
        color_list = self.find_all(
            element=product,
            locator=comm_locators.color_element
        )
        add_to_cart_button = self.find(comm_locators.add_to_cart_button)
        actions = ActionChains(self.driver)
        actions.move_to_element(product)
        actions.move_to_element(size_list[0])
        actions.click()
        actions.move_to_element(color_list[0])
        actions.click()
        actions.move_to_element(add_to_cart_button)
        actions.click()
        actions.perform()
        WebDriverWait(self.driver, 2).until(
            EC.text_to_be_present_in_element(comm_locators.counter_number, "1")
        )
        counter_number = self.find(comm_locators.counter_number)
        assert counter_number.text == "1"

    def go_to_product_page(self):
        all_products = self.find_all(comm_locators.product)
        random_product = all_products[
            random.randint(0, len(all_products) - 1)
        ]
        product_name = self.find(
            element=random_product,
            locator=comm_locators.product_name
        ).text
        random_product.click()
        h1_text = self.find(comm_locators.tag_h1)
        assert h1_text.text == product_name
