from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class AccountCreatedPage(BasePage):
    account_created_text = (By.XPATH, "//b[text()='Account Created!']")
    continue_button = (By.XPATH, "//a[@data-qa='continue-button']")

    def wait_for_account_created(self):
        self.wait.until(EC.visibility_of_element_located(self.account_created_text))

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
