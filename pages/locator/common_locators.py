from selenium.webdriver.common.by import By

tag_h1 = (By.TAG_NAME, "h1")
logo = (By.CSS_SELECTOR, "a.logo")

registration_button = (By.LINK_TEXT, "Create an Account")

# Products locators
product = (By.CSS_SELECTOR, "li.item.product.product-item")
product_name = (By.CSS_SELECTOR, ".product.name.product-item-name")
size_element = (By.CSS_SELECTOR, ".swatch-option.text")
color_element = (By.CSS_SELECTOR, ".swatch-option.color")
add_to_cart_button = (By.CSS_SELECTOR, "button[title='Add to Cart']")
counter_number = (By.CLASS_NAME, "counter-number")

# search locators
search_field = (By.ID, "search")
search_result_message = (By.CSS_SELECTOR, ".message.notice")
