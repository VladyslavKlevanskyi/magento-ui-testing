import os

from dotenv import load_dotenv
from faker import Faker

fake = Faker()

load_dotenv()

BASE_URL = "https://magento.softwaretestingboard.com/"
CREATE_ACCOUNT_URL = "customer/account/create/"

EXISTING_USER_DATA = {
    "first_name": os.getenv("first_name"),
    "last_name": os.getenv("last_name"),
    "email": os.getenv("email"),
    "password": os.getenv("password")
}

VALID_DATA = {
    "first_name": fake.first_name(),
    "last_name": fake.last_name(),
    "email": fake.email(),
    "password": fake.password()
}

INVALID_DATA = {
    "first_name": "",
    "last_name": "",
    "email": "email",
    "password": "test",
    "password_conf": "Test"
}
MESSAGES = {
    "successful_registration": "Thank you for registering with Main "
                               "Website Store.",
    "required_field": "This is a required field.",
    "enter_valid_email": "Please enter a valid email address "
                         "(Ex: johndoe@domain.com).",
    "pass_strength_weak": "Weak",
    "pass_strength_medium": "Medium",
    "pass_strength_strong": "Strong",
    "pass_strength_very_strong": "Very Strong",
    "minimum_pass_length": "Minimum length of this field must be equal or "
                           "greater than 8 symbols. Leading and trailing "
                           "spaces will be ignored.",
    "password_mismatch": "Please enter the same value again."
}
