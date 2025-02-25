from data import CREATE_ACCOUNT_URL
from pages.base_page import BasePage
from pages.locator import create_account_locators as locators


class CreateAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = CREATE_ACCOUNT_URL

    def fill_out_and_submit_form(self, first_name, last_name, email, password):
        first_name_field = self.find(locator=locators.first_name)
        last_name_field = self.find(locator=locators.last_name)
        email_field = self.find(locator=locators.email)
        password_field = self.find(locator=locators.password)
        password_confirmation_field = self.find(
            locator=locators.password_confirmation
        )
        submit_button = self.find(locator=locators.submit_button)

        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirmation_field.send_keys(password)
        submit_button.click()

    def check_alert_text_is(self, text):
        alert = self.find(locator=locators.successful_registration_alert)
        assert alert.text == text

