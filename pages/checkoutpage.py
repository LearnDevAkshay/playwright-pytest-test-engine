from playwright.sync_api import expect

from pages.basepage import BasePage

import allure


inventory_item = "//div[@class='inventory_item_name']"
checkout_button = "#checkout"
first_name = "#first-name"
last_name = "#last-name"
postal_code = "#postal-code"
continue_button = "#continue"
finish_button = "#finish"
confirmation_message = "//h2[normalize-space()='Thank you for your order!']"


class CheckoutPage(BasePage):

    def __init__(self, page_instance):

        super().__init__(page_instance)

        self.page = page_instance

    @allure.step("Verify Added Item")
    def verify_added_item(self, td1):

        item_in_cart = self.get_text(inventory_item)

        expect(self.page.locator(inventory_item)).to_have_text(
            td1["Item"]
        )

        return self

    @allure.step("Check out the item")
    def check_out_item(self):

        self.click(checkout_button)

        return self

    @allure.step("Enter Address Details")
    def enter_address_details(self, td1):

        self.type(first_name, td1["FirstName"])

        self.type(last_name, td1["LastName"])

        self.type(postal_code, td1["PostalCode"])

        return self

    @allure.step("Click on Continue Button")
    def click_on_continue_button(self):

        self.click(continue_button)

        return self

    @allure.step("Click on Finish Button")
    def click_on_finish_button(self):

        self.click(finish_button)

        return self

    @allure.step("Verify Confirmation Message")
    def verify_confirmation_message(self):

        expect(
            self.page.locator(confirmation_message)
        ).to_have_text(
            "Thank you for your order!"
        )

        return self