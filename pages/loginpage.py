from playwright.sync_api import expect

from pages.basepage import BasePage

from utils.read_config_file import read_config

import allure


user_name = "#user-name"
input_password = "#password"
login_button = "#login-button"


class LoginPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.page = page



    @allure.step("Login to the application")
    def login(self):

        env, browser, logging, headless_mode, url, email, password = read_config()

        self.open_url(url)

        self.type(user_name, email)

        self.type(input_password, password)

        self.click(login_button)

        expect(self.page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )