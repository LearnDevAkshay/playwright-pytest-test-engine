from pages.basepage import BasePage

import allure


add_to_cart_link = (
    lambda product:
    f"//div[contains(text(),'{product}')]"
    f"//ancestor::div[2]//button[contains(text(),'Add to cart')]"
)

cart_link = "//a[@class='shopping_cart_link']"


class HomePage(BasePage):

    def __init__(self, page_instance):

        super().__init__(page_instance)

        self.page = page_instance

    @allure.step("Add Bag Pack To Cart")
    def add_back_pack_to_cart(self, td1):

        self.click(add_to_cart_link(td1["Item"]))

        return self

    @allure.step("Click on Cart")
    def click_on_cart(self):

        self.click(cart_link)

        return self