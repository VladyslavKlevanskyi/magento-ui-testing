from time import sleep

import pytest
from selenium import webdriver

from pages.create_account import CreateAccount


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(2)
    yield chrome_driver
    sleep(3)
    chrome_driver.quit()


@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)
