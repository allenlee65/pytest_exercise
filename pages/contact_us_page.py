from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class ContactUsPage(BasePage):
    get_in_touch_header = (By.XPATH, "//h2[contains(text(), 'Get In Touch')]")
    name_input = (By.NAME, "name")
    email_input = (By.NAME, "email")
    subject_input = (By.NAME, "subject")
    message_textarea = (By.NAME, "message")
    upload_file_input = (By.NAME, "upload_file")
    submit_button = (By.XPATH, '//*[@id="contact-us-form"]/div[6]/input')
    success_message = (By.XPATH, "//div[contains(text(), 'Success! Your details have been submitted successfully.')]")
    home_button = (By.LINK_TEXT, "Home")

    def wait_for_get_in_touch(self):
        self.wait.until(EC.visibility_of_element_located(self.get_in_touch_header))

    def fill_contact_form(self, name, email, subject, message, file_path):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.subject_input).send_keys(subject)
        self.driver.find_element(*self.message_textarea).send_keys(message)
        self.driver.find_element(*self.upload_file_input).send_keys(file_path)

    def submit_form(self):
        self.driver.execute_script("window.scrollBy(0,200);")
        self.driver.find_element(*self.submit_button).click()

    def accept_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass

    def wait_for_success_message(self):
        self.wait.until(EC.visibility_of_element_located(self.success_message))

    def go_home(self):
        self.driver.find_element(*self.home_button).click()
