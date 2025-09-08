from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class AccountCreationPage(BasePage):
    account_info_header = (By.XPATH, "//b[text()='Enter Account Information']")
    title_mr_radio = (By.ID, "id_gender1")
    password_input = (By.ID, "password")
    days_select = (By.ID, "days")
    months_select = (By.ID, "months")
    years_select = (By.ID, "years")
    newsletter_checkbox = (By.ID, "newsletter")
    optin_checkbox = (By.ID, "optin")
    first_name_input = (By.ID, "first_name")
    last_name_input = (By.ID, "last_name")
    company_input = (By.ID, "company")
    address1_input = (By.ID, "address1")
    address2_input = (By.ID, "address2")
    country_input = (By.ID, "country")
    state_input = (By.ID, "state")
    city_input = (By.ID, "city")
    zipcode_input = (By.ID, "zipcode")
    mobile_number_input = (By.ID, "mobile_number")
    create_account_button = (By.XPATH, "//button[@data-qa='create-account']")

    def wait_for_account_info(self):
        self.wait.until(EC.visibility_of_element_located(self.account_info_header))

    def fill_account_info(
        self,
        password,
        first_name,
        last_name,
        company,
        address1,
        address2,
        country,
        state,
        city,
        zipcode,
        mobile_number,
    ):
        self.wait_for_account_info()
        self.driver.execute_script("window.scrollBy(0,400);")
        self.driver.find_element(*self.title_mr_radio).click()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.days_select).send_keys("1")
        self.driver.find_element(*self.months_select).send_keys("January")
        self.driver.find_element(*self.years_select).send_keys("2000")
        self.driver.find_element(*self.newsletter_checkbox).click()
        self.driver.find_element(*self.optin_checkbox).click()
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.company_input).send_keys(company)
        self.driver.find_element(*self.address1_input).send_keys(address1)
        self.driver.find_element(*self.address2_input).send_keys(address2)
        self.driver.find_element(*self.country_input).send_keys(country)
        self.driver.find_element(*self.state_input).send_keys(state)
        self.driver.find_element(*self.city_input).send_keys(city)
        self.driver.find_element(*self.zipcode_input).send_keys(zipcode)
        self.driver.find_element(*self.mobile_number_input).send_keys(mobile_number)

    def submit_create_account(self):
        self.driver.find_element(*self.create_account_button).click()
