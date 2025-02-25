from data import VALID_DATA


def test_create_account_with_valid_data(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_out_and_submit_form(
        first_name=VALID_DATA["first_name"],
        last_name=VALID_DATA["last_name"],
        email=VALID_DATA["email"],
        password=VALID_DATA["password"]
    )
    create_account_page.check_alert_text_is(
        "Thank you for registering with Main Website Store."
    )
