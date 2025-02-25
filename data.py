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
