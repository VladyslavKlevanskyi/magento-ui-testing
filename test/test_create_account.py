import pytest

from data import (
    VALID_DATA,
    INVALID_DATA,
    MESSAGES,
    INVALID_EMAIL,
    PASS_STRENGTH
)


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


@pytest.mark.critical
def test_first_and_last_name_fields_are_required(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_out_and_submit_form(
        email=VALID_DATA["email"],
        password=VALID_DATA["password"],
    )
    create_account_page.check_field_alert_is(
        field_name="First Name",
        message=MESSAGES["required_field"]
    )
    create_account_page.check_field_alert_is(
        field_name="Last Name",
        message=MESSAGES["required_field"]
    )


@pytest.mark.critical
@pytest.mark.parametrize(
    argnames="email, message",
    argvalues=[data[1] for data in INVALID_EMAIL],
    ids=[title[0] for title in INVALID_EMAIL]
)
def test_email_field_validation(create_account_page, email, message):
    create_account_page.open_page()
    create_account_page.fill_out_and_submit_form(
        first_name=VALID_DATA["first_name"],
        last_name=VALID_DATA["last_name"],
        email=email,
        password=VALID_DATA["password"],
    )
    create_account_page.check_field_alert_is(
        field_name="Email",
        message=message
    )


@pytest.mark.medium
@pytest.mark.parametrize(
    argnames="password, message",
    argvalues=[data[1] for data in PASS_STRENGTH],
    ids=[title[0] for title in PASS_STRENGTH]
)
def test_password_strength_validation(create_account_page, password, message):
    create_account_page.open_page()
    create_account_page.fill_out_password_field(password=password)
    create_account_page.check_field_alert_is(
        field_name="Pass Strength",
        message=message
    )
