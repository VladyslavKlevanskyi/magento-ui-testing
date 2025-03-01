from selenium.webdriver import Keys
from data.urls import CREATE_ACCOUNT_URL
from pages.base_page import BasePage
from pages.locator import create_account_locators as locators


class CreateAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = CREATE_ACCOUNT_URL

    def enter_first_name(self, first_name: str):
        first_name_field = self.find(locator=locators.first_name)
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name: str):
        last_name_field = self.find(locator=locators.last_name)
        last_name_field.send_keys(last_name)

    def enter_email(self, email: str):
        email_field = self.find(locator=locators.email)
        email_field.send_keys(email)

    def enter_password(self, password: str):
        password_field = self.find(locator=locators.password)
        password_field.send_keys(password)

    def enter_password_confirmation(self, password: str):
        password_confirmation_field = self.find(
            locator=locators.password_confirmation
        )
        password_confirmation_field.send_keys(password)

    def click_create_an_account_button(self):
        submit_button = self.find(locator=locators.submit_button)
        submit_button.click()

    def check_successful_account_creation_alert_is(self, text):
        alert = self.find(locator=locators.successful_registration_alert)
        assert alert.text == text

    def check_field_alert_is(self, field_name: str, message: str):
        alert = None
        if field_name == "First Name":
            alert = self.find(locator=locators.first_name_alert)
        elif field_name == "Last Name":
            alert = self.find(locator=locators.last_name_alert)
        elif field_name == "Email":
            alert = self.find(locator=locators.email_alert)
        elif field_name == "Pass":
            alert = self.find(locator=locators.password_alert)
        elif field_name == "Pass Strength":
            alert = self.find(locator=locators.password_strength_meter)
        elif field_name == "Pass Confirmation":
            alert = self.find(locator=locators.password_conf_alert)
        assert alert.text == message
