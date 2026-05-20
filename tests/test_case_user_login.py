import pytest
import allure
import utils
from pages.loginpage import LoginPage



# File read
# Base Page - Done
# Common Module
# Global - Done
# Logging - Done
# Listeners - Done
# Utils

@pytest.mark.usefixtures("getdata")
@allure.suite("Login")
class TestLogin:

    @allure.description(
        "1. Navigate user login page "
        "2. Enter user email "
        "3. Enter user password "
        "4. Click on Submit button"
    )
    @pytest.mark.all
    def test_case_user_login(self, page_instance):

        login_page = LoginPage(page_instance)

        login_page.login()
