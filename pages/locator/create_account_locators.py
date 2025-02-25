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
