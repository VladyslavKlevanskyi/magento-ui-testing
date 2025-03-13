from data.urls import CREATE_ACCOUNT_URL
from pages.base_page import BasePage
from pages.locator import create_account_locators as locators


class CreateAccount(BasePage):
    """
    A page object representing the 'Create Account' page.
    Provides methods for interacting with the registration form.
    """
    def __init__(self, driver):
        """
        Initializes the CreateAccount page with a WebDriver instance.

        Args:
            driver: WebDriver instance controlling the browser.
        """
        super().__init__(driver)
        self.page_url = CREATE_ACCOUNT_URL

    def enter_first_name(self, first_name: str) -> None:
        """
        Enters the first name into the first name input field.

        Args:
            first_name (str): The user's first name.
        """
        # Locate the first name input field and enter the first name
        first_name_field = self.find(locator=locators.first_name)
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        """
        Enters the last name into the last name input field.

        Args:
            last_name (str): The user's last name.
        """
        # Locate the last name input field and enter the last name
        last_name_field = self.find(locator=locators.last_name)
        last_name_field.send_keys(last_name)

    def enter_email(self, email: str) -> None:
        """
        Enters the email into the email input field.

        Args:
            email (str): The user's email address.
        """
        # Locate the email input field and enter the email
        email_field = self.find(locator=locators.email)
        email_field.send_keys(email)

    def enter_password(self, password: str) -> None:
        """
        Enters the provided password into the password input field.

        This method types the password character by character to simulate
        a more realistic user input. It finds the password field using the
        predefined locator and sends the password characters sequentially.

        :param password: The password string to be entered into the input field
        """
        # Locate the password input field using the locator from locators
        password_field = self.find(locator=locators.password)

        # Iterate through each character in the password and enter
        # it into the field
        for letter in password:
            password_field.send_keys(letter)

    def enter_password_confirmation(self, password: str) -> None:
        """
        Enters the password confirmation into the confirmation input field.

        Args:
            password (str): The user's chosen password
            (same as in 'enter_password').
        """
        # Locate the password confirmation input field and enter the
        # same password
        password_confirmation_field = self.find(
            locator=locators.password_confirmation
        )
        password_confirmation_field.send_keys(password)

    def click_create_an_account_button(self) -> None:
        """
        Clicks the 'Create an Account' button to submit the form.
        """
        # Locate and click the 'Create an Account' button
        submit_button = self.find(locator=locators.submit_button)
        submit_button.click()

    def check_successful_account_creation_alert_is(self, text) -> None:
        """
        Verifies that the success message is displayed after account creation.

        Args:
            text (str): Expected success message text.
        """
        # Locate the success alert element
        alert = self.find(locator=locators.successful_registration_alert)

        # Verify that the displayed success message matches the expected text
        assert alert.text == text

    def check_field_alert_is(self, field_name: str, message: str) -> None:
        """
        Checks that the correct validation message is displayed for a
        given field.

        Args:
            field_name (str): The name of the field to check.
            message (str): The expected validation message.
        """
        # Initialize alert as None
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

        # Verify that the expected validation message is displayed
        assert alert.text == message
