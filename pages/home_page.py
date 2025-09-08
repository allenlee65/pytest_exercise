from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    URL = "http://automationexercise.com"

    signup_login_link = (By.LINK_TEXT, "Signup / Login")
    contact_us_link = (By.LINK_TEXT, "Contact us")
    products_link = (By.CSS_SELECTOR, "a[href='/products']")
    cart_link = (By.CSS_SELECTOR, "a[href='/view_cart']")

    def open(self):
        self.driver.get(self.URL)

    def go_to_signup_login(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_login_link)).click()

    def go_to_contact_us(self):
        self.wait.until(EC.element_to_be_clickable(self.contact_us_link)).click()

    def go_to_products(self):
        self.wait.until(EC.element_to_be_clickable(self.products_link)).click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_link)).click()
