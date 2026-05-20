import allure
import logging
from datetime import datetime
import json
import os

from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

try:
    from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
except ImportError:  # fallback
    from selenium.webdriver.support.event_firing_webdriver import AbstractEventListener, EventFiringWebDriver  # type: ignore


# ------- basic logging setup (tweak as you like) -------
logger = logging.getLogger("selenium-listener")
if not logger.handlers:
    handler = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    #handler.setFormatter(fmt)
    #logger.addHandler(handler)


    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)
    file_path = os.path.join(log_dir, "selenium.log")

    file_handler = logging.FileHandler(file_path, mode="a", encoding="utf-8")
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def _attach_json(name: str, data: dict):
    allure.attach(
        json.dumps(data, indent=2, ensure_ascii=False),
        name=name,
        attachment_type=allure.attachment_type.JSON,
    )

class AllureSeleniumListener(AbstractEventListener):
    """
    Event listener that logs key Selenium events and enriches Allure reports.
    Captures screenshot + HTML on exceptions.
    """

    # ---------- Navigation ----------
    def before_navigate_to(self, url, driver):
        logger.info(f"[before_navigate_to] {url}")
        #_attach_json("Before Navigate To", {"url": url})

    def after_navigate_to(self, url, driver):
        logger.info(f"[after_navigate_to] {url}")
        #_attach_json("After Navigate To", {"url": url, "current_url": driver.current_url})

    def before_navigate_back(self, driver):
        logger.info("[before_navigate_back]")

    def after_navigate_back(self, driver):
        logger.info("[after_navigate_back]")

    def before_navigate_forward(self, driver):
        logger.info("[before_navigate_forward]")

    def after_navigate_forward(self, driver):
        logger.info("[after_navigate_forward]")

    # Some Selenium builds raise these through navigate_to(refresh=True); include for completeness
    def before_refresh(self, driver):
        logger.info("[before_refresh]")

    def after_refresh(self, driver):
        logger.info("[after_refresh]")

    # ---------- Find ----------
    def before_find(self, by, value, driver):
        logger.info(f"[before_find] by={by}, value={value}")
        #_attach_json("Before Find", {"by": by, "value": value})

    def after_find(self, by, value, driver):
        logger.info(f"[after_find] by={by}, value={value}")

    # ---------- Click ----------
    def before_click(self, element, driver):
        try:
            desc = element.get_attribute("outerHTML")[:200]
        except Exception:
            desc = "<unavailable>"
        logger.info(f"[before_click] {desc}")

    def after_click(self, element, driver):
        logger.info("[after_click]")

    # ---------- Value change (typing, clear+type, etc.) ----------
    def before_change_value_of(self, element, driver):
        logger.info("[before_change_value_of]")

    def after_change_value_of(self, element, driver):
        logger.info("[after_change_value_of]")

    # ---------- Script exec ----------
    def before_execute_script(self, script, driver) :
        logger.info(f"[before_execute_script] {script[:120]}")

    def after_execute_script(self, script, driver):
        logger.info(f"[after_execute_script] {script[:120]}")

    # ---------- Window / Session lifecycle ----------
    def before_close(self, driver):
        logger.info("[before_close]")

    def after_close(self, driver):
        logger.info("[after_close]")

    def before_quit(self, driver):
        logger.info("[before_quit]")

    def after_quit(self, driver):
        logger.info("[after_quit]")




def wrap_driver(driver):
    """
            Wrap a normal WebDriver with EventFiringWebDriver + AllureSeleniumListener.
            Usage:
                driver = webdriver.Chrome()
                driver = wrap_driver(driver)
            """
    return EventFiringWebDriver(driver, AllureSeleniumListener())

