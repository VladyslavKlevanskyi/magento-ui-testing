import pytest

from data import VALID_DATA, INVALID_DATA, MESSAGES


@pytest.mark.smoke
def test_create_account_with_valid_data(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_out_and_submit_form(
        first_name=VALID_DATA["first_name"],
        last_name=VALID_DATA["last_name"],
        email=VALID_DATA["email"],
        password=VALID_DATA["password"]
    )
    create_account_page.check_successful_account_creation_alert_is(
        MESSAGES["successful_registration"]
    )


@pytest.mark.smoke
def test_create_account_with_invalid_data(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_out_and_submit_form(
        first_name=INVALID_DATA["first_name"],
        last_name=INVALID_DATA["last_name"],
        email=INVALID_DATA["email"],
        password=INVALID_DATA["password"],
        password_confirmation=INVALID_DATA["password_conf"]
    )
    create_account_page.check_field_alert_is(
        field_name="First Name",
        message=MESSAGES["required_field"]
    )
    create_account_page.check_field_alert_is(
        field_name="Last Name",
        message=MESSAGES["required_field"]
    )
    create_account_page.check_field_alert_is(
        field_name="Email",
        message=MESSAGES["enter_valid_email"]
    )
    create_account_page.check_field_alert_is(
        field_name="Pass Strength",
        message=MESSAGES["pass_strength_weak"]
    )
    create_account_page.check_field_alert_is(
        field_name="Pass",
        message=MESSAGES["minimum_pass_length"]
    )
    create_account_page.check_field_alert_is(
        field_name="Pass Confirmation",
        message=MESSAGES["password_mismatch"]
    )
