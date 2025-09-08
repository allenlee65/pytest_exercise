import random
import string
import pytest
import os

from selenium.webdriver.chrome.webdriver import WebDriver

from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.account_creation_page import AccountCreationPage
from pages.account_created_page import AccountCreatedPage
from pages.user_dashboard_page import UserDashboardPage
from pages.contact_us_page import ContactUsPage


class TestAutomationExercise:

    def generate_random_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"test_{random_string}@example.com"

    def generate_random_name(self):
        names = ["John", "Jane", "Mike", "Sarah", "David", "Emma", "Alex", "Lisa"]
        return random.choice(names) + str(random.randint(100, 999))

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("driver")
    @pytest.mark.usefixtures("base_url")
    @pytest.mark.usefixtures("credentials")
    def test_register_user(self, driver: WebDriver):
        home = HomePage(driver)
        home.open()
        assert "Automation Exercise" in home.driver.title
        home.go_to_signup_login()

        signup_login = SignupLoginPage(driver)
        signup_login.wait_for_new_user_signup()

        username = self.generate_random_name()
        email = self.generate_random_email()
        signup_login.signup(username, email)

        account_creation = AccountCreationPage(driver)
        account_creation.fill_account_info(
            password="TestPassword123",
            first_name="Test",
            last_name="User",
            company="TestCompany",
            address1="123 Test St",
            address2="Suite 1",
            country="United States",
            state="TestState",
            city="TestCity",
            zipcode="12345",
            mobile_number="1234567890",
        )
        account_creation.submit_create_account()

        account_created = AccountCreatedPage(driver)
        account_created.wait_for_account_created()
        account_created.click_continue()

        dashboard = UserDashboardPage(driver)
        dashboard.wait_for_user_logged_in()

        dashboard.delete_account()
        dashboard.wait_for_account_deleted()
        dashboard.click_continue_after_delete()

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("driver")
    @pytest.mark.usefixtures("base_url")
    @pytest.mark.usefixtures("credentials")
    def test_login_with_correct_credentials(self, driver: WebDriver):
        home = HomePage(driver)
        home.open()
        home.go_to_signup_login()

        email = os.getenv('AE_TEST_EMAIL')
        password = os.getenv('AE_TEST_PASSWORD')
        login = SignupLoginPage(driver)
        login.wait_for_login_to_account()
        login.login(email, password)

        dashboard = UserDashboardPage(driver)
        dashboard.wait_for_user_logged_in()

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("driver")
    @pytest.mark.usefixtures("base_url")
    @pytest.mark.usefixtures("credentials")
    def test_login_with_incorrect_credentials(self, driver: WebDriver):
        home = HomePage(driver)
        home.open()
        home.go_to_signup_login()

        login = SignupLoginPage(driver)
        login.wait_for_login_to_account()
        login.login("invalid@example.com", "wrongpassword")

        assert login.is_error_message_displayed()

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("driver")
    @pytest.mark.usefixtures("base_url")
    @pytest.mark.usefixtures("credentials")
    def test_contact_us_form(self, driver: WebDriver):
        import tempfile
        import os

        home = HomePage(driver)
        home.open()
        home.go_to_contact_us()

        contact_us = ContactUsPage(driver)
        contact_us.wait_for_get_in_touch()

        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as temp_file:
            temp_file.write("Test file content")
            temp_file_path = temp_file.name

        contact_us.fill_contact_form(
            name="Test User",
            email="test@example.com",
            subject="Test Subject",
            message="This is a test message for automation testing.",
            file_path=temp_file_path,
        )
        contact_us.submit_form()
        contact_us.accept_alert()
        contact_us.wait_for_success_message()
        contact_us.go_home()

        os.unlink(temp_file_path)  # Cleanup temp file

# Additional test methods can follow here using page objects.

if __name__ == "__main__":
    pytest.main()
