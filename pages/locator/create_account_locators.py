first_name = ("id", "firstname")
last_name = ("id", "lastname")
email = ("id", "email_address")
password = ("id", "password")
password_confirmation = ("id", "password-confirmation")
submit_button = ("xpath", "//*[@title='Create an Account']")
successful_registration_alert = (
    "xpath", "//*[@data-bind='html: "
             "$parent.prepareMessageForHtml(message.text)']"
)
first_name_alert = ("id", "firstname-error")
last_name_alert = ("id", "lastname-error")
email_alert = ("id", "email_address-error")
password_strength_meter = ("id", "password-strength-meter-label")
password_alert = ("id", "password-error")
password_conf_alert = ("id", "password-confirmation-error")
