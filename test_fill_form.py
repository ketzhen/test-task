import random

import pytest

from config import BASE_URL
from form_page import FormPage


class TestFillForm:
    @pytest.fixture()
    def setup(self, browser):
        self.form_page = FormPage(browser, BASE_URL)

    def test_fill_form(self, setup):
        self.form_page.open_page()
        self.form_page.input_first_name()
        self.form_page.input_last_name()
        self.form_page.female_sex_click()
        self.form_page.experience_click(random.randint(1, 7))
        self.form_page.input_date()
        self.form_page.automation_click()
        self.form_page.upload_file()
        self.form_page.selenium_click()
        self.form_page.select_europe()
        self.form_page.select_command()
        self.form_page.button_click()