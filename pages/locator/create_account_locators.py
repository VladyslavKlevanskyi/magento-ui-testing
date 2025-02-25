from selenium.webdriver.common.by import By

first_name = (By.ID, "firstname")
last_name = (By.ID, "lastname")
email = (By.ID, "email_address")
password = (By.ID, "password")
password_confirmation = (By.ID, "password-confirmation")
submit_button = (By.XPATH, "//*[@title='Create an Account']")
successful_registration_alert = (
    By.XPATH,
    "//*[@data-bind='html: $parent.prepareMessageForHtml(message.text)']"
)
first_name_alert = (By.ID, "firstname-error")
last_name_alert = (By.ID, "lastname-error")
email_alert = (By.ID, "email_address-error")
password_strength_meter = (By.ID, "password-strength-meter-label")
password_alert = (By.ID, "password-error")
password_conf_alert = (By.ID, "password-confirmation-error")
