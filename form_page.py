import os
from datetime import datetime
import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page import BasePage


class FormPage(BasePage):
    NAME_FIELD = (By.NAME, "firstname")
    SURNAME_FIELD = (By.NAME, "lastname")
    FEMALE_SEX_RADIO = (By.CSS_SELECTOR, '[value="Female"]')
    EXPERIENCE_RADIO = '[value="{}"]'
    DATE_FIELD = (By.CSS_SELECTOR, 'tr:nth-child(5) td:nth-child(2) input')
    AUTOMATION_TESTER_FIELD = (By.CSS_SELECTOR, '[value="Automation Tester"]')
    UPLOAD_FILE = (By.CSS_SELECTOR, '[type="file"]')
    SELENIUM_CHECKBOX = (By.CSS_SELECTOR, '[value="Selenium Webdriver"]')
    CONTINENTS_LIST = (By.NAME, "continents")
    COMMANDS_LIST = (By.NAME, "selenium_commands")
    BUTTON = (By.NAME, "submit")

    def input_first_name(self):
        name = ''.join(random.choices(string.ascii_lowercase, k=5))
        self.wait_until_clickable(self.NAME_FIELD).send_keys(name)

    def input_last_name(self):
        last_name = ''.join(random.choices(string.ascii_lowercase, k=5))
        self.wait_until_clickable(self.SURNAME_FIELD).send_keys(last_name)

    def female_sex_click(self):
        self.wait_until_clickable(self.FEMALE_SEX_RADIO).click()

    def experience_click(self, number: int):
        self.wait_until_clickable((By.CSS_SELECTOR, self.EXPERIENCE_RADIO.format(number))).click()

    def automation_click(self):
        self.wait_until_clickable(self.AUTOMATION_TESTER_FIELD).click()

    def input_date(self):
        self.wait_until_clickable(self.DATE_FIELD).send_keys(datetime.now().strftime("%m/%d/%Y"))

    def upload_file(self):
        self.wait_until_clickable(self.UPLOAD_FILE).send_keys(os.path.join(os.getcwd(), "Koala.jpeg"))

    def selenium_click(self):
        self.wait_until_clickable(self.SELENIUM_CHECKBOX).click()

    def select_europe(self):
        element = self.wait_until_clickable(self.CONTINENTS_LIST)
        select = Select(element)
        select.select_by_visible_text("Europe")

    def select_command(self):
        element = self.wait_until_clickable(self.COMMANDS_LIST)
        select = Select(element)
        select.select_by_visible_text("Wait Commands")

    def button_click(self):
        self.wait_until_clickable(self.BUTTON).click()



