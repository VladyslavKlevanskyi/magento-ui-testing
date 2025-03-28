import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.create_account import CreateAccount
from pages.eco_friendly import CollectionsEcoFriendly
from pages.sale import Sale


@pytest.fixture()
def driver():
    chrome_options = Options()
    # chrome_options.add_argument('start-maximized')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    # Bypass OS security model, required for running in CI environments
    chrome_options.add_argument("--no-sandbox")  # For GitHub actions

    # Use /tmp instead of /dev/shm to avoid limited memory space issues
    chrome_options.add_argument("--disable-dev-shm-usage")  # For GitHub action

    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.implicitly_wait(2)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def create_account_page(driver):
    return CreateAccount(driver)


@pytest.fixture()
def collections_eco_friendly_page(driver):
    return CollectionsEcoFriendly(driver)


@pytest.fixture()
def sale_page(driver):
    return Sale(driver)
