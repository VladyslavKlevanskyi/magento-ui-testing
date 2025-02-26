from time import sleep

import pytest
from selenium import webdriver

from pages.create_account import CreateAccount
from pages.eco_friendly import CollectionsEcoFriendly


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(2)
    yield chrome_driver
    # sleep(3)
    chrome_driver.quit()


@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)


@pytest.fixture()
def collections_eco_friendly_page(driver):
    return CollectionsEcoFriendly(driver)
