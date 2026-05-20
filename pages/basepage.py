
import os, time

class BasePage:

    def __init__(self, page):
        self.page = page

    def open_url(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def type(self, locator, text):
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    # ----------------------------
    # Screenshots
    # ----------------------------
    def take_screenshot(self, name="screenshot"):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        path = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(path, exist_ok=True)
        self.driver.save_screenshot(os.path.join(path, filename))
        return os.path.join(path, filename)

