from typing import Tuple

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser: Chrome, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def wait_until_clickable(self, locator: Tuple, timeout: int = 10) -> WebElement:
        element = WebDriverWait(self.browser, timeout).until(ec.element_to_be_clickable(locator))
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        return element
