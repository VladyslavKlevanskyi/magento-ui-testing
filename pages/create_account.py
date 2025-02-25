from data import CREATE_ACCOUNT_URL
from pages.base_page import BasePage
from pages.locator import create_account_locators as locators


class CreateAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = CREATE_ACCOUNT_URL

    def fill_out_and_submit_form(
            self,
            first_name: str,
            last_name: str,
            email: str,
            password: str,
            password_confirmation: str = None,
    ) -> None:
        if password_confirmation is None:
            password_confirmation = password
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
        password_confirmation_field.send_keys(password_confirmation)
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

