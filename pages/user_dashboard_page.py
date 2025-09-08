from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class UserDashboardPage(BasePage):
    logged_in_as_text = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    delete_account_link = (By.LINK_TEXT, "Delete Account")
    account_deleted_text = (By.XPATH, "//b[text()='Account Deleted!']")
    continue_button_after_delete = (By.XPATH, "//a[@data-qa='continue-button']")

    def wait_for_user_logged_in(self):
        self.wait.until(EC.visibility_of_element_located(self.logged_in_as_text))

    def delete_account(self):
        self.driver.find_element(*self.delete_account_link).click()

    def wait_for_account_deleted(self):
        self.wait.until(EC.visibility_of_element_located(self.account_deleted_text))

    def click_continue_after_delete(self):
        self.driver.find_element(*self.continue_button_after_delete).click()
