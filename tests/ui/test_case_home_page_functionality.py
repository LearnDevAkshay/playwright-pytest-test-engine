import pytest
import allure

from pages.checkoutpage import CheckoutPage
from pages.homepage import HomePage
from pages.loginpage import LoginPage


# File read
# Base Page - Done
# Common Module
# Global - Done
# Logging - Done
# Listeners - Done
# Utils


@pytest.mark.usefixtures("getdata")
@allure.suite("HomePage")
class TestHomePageFunctionality:

    @allure.description(
        "1. Navigate user login page "
        "2. Add Item to Cart "
        "3. Checkout the item "
        "4. Add address details "
        "5. Place an order"
    )
    @pytest.mark.all
    def test_add_bag_pack_to_cart(self, page_instance):

        login_page = LoginPage(page_instance)

        home_page = HomePage(page_instance)

        checkout_page = CheckoutPage(page_instance)

        td1 = self.td1

        login_page.login()

        (
            home_page
            .add_back_pack_to_cart(td1)
            .click_on_cart()
        )

        (
            checkout_page
            .verify_added_item(td1)
            .check_out_item()
            .enter_address_details(td1)
            .click_on_continue_button()
            .click_on_finish_button()
            .verify_confirmation_message()
        )

    @allure.description(
        "1. Navigate user login page "
        "2. Add Item to Cart "
        "3. Checkout the item "
        "4. Add address details "
        "5. Place an order"
    )
    @pytest.mark.all
    def test_add_bike_light_to_cart(self, page_instance):

        login_page = LoginPage(page_instance)

        home_page = HomePage(page_instance)

        checkout_page = CheckoutPage(page_instance)

        td1 = self.td1

        login_page.login()

        (
            home_page
            .add_back_pack_to_cart(td1)
            .click_on_cart()
        )

        (
            checkout_page
            .verify_added_item(td1)
            .check_out_item()
            .enter_address_details(td1)
            .click_on_continue_button()
            .click_on_finish_button()
            .verify_confirmation_message()
        )