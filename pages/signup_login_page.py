from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class SignupLoginPage(BasePage):
    signup_name_input = (By.NAME, "name")
    signup_email_input = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_button = (By.XPATH, "//button[@data-qa='signup-button']")
    login_email_input = (By.XPATH, "//input[@data-qa='login-email']")
    login_password_input = (By.XPATH, "//input[@data-qa='login-password']")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")
    new_user_signup_header = (By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
    login_to_account_header = (By.XPATH, "//h2[contains(text(), 'Login to your account')]")
    login_error_message = (By.XPATH, "//p[contains(text(), 'Your email or password is incorrect!')]")

    def wait_for_new_user_signup(self):
        self.wait.until(EC.visibility_of_element_located(self.new_user_signup_header))

    def wait_for_login_to_account(self):
        self.wait.until(EC.visibility_of_element_located(self.login_to_account_header))

    def signup(self, name, email):
        self.wait_for_new_user_signup()
        self.driver.find_element(*self.signup_name_input).clear()
        self.driver.find_element(*self.signup_name_input).send_keys(name)
        self.driver.find_element(*self.signup_email_input).clear()
        self.driver.find_element(*self.signup_email_input).send_keys(email)
        self.driver.find_element(*self.signup_button).click()

    def login(self, email, password):
        self.wait_for_login_to_account()
        email_field = self.driver.find_element(*self.login_email_input)
        email_field.clear()
        email_field.send_keys(email)
        password_field = self.driver.find_element(*self.login_password_input)
        password_field.clear()
        password_field.send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_error_message_displayed(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.login_error_message)).is_displayed()
        except:
            return False
