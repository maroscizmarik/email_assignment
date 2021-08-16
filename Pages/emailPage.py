import time

from Locators.emailPageLocators import Locators
from selenium.webdriver.common.keys import Keys


class EmailPage:
    def __init__(self, driver):
        self.driver = driver

        self.compose_btn = Locators.compose_btn_css
        self.recipient_input_field = Locators.recipient_input_field_name
        self.subject_input_field = Locators.subject_input_field_name
        self.body_input_field = Locators.body_input_css
        self.send_btn = Locators.send_btn_css
        self.user_menu_btn = Locators.user_menu_btn_css
        self.logout_btn = Locators.logout_btn_css

    def click_compose_btn(self):
        self.driver.find_element_by_css_selector(self.compose_btn).click()

    def enter_recipient(self, recipient):
        self.driver.find_element_by_name(self.recipient_input_field).send_keys(recipient)
        time.sleep(2)
        self.driver.find_element_by_name(self.recipient_input_field).send_keys(Keys.ENTER)

    def enter_subject(self, subject):
        self.driver.find_element_by_name(self.subject_input_field).send_keys(subject)

    def enter_email_text(self, email_text):
        self.driver.find_element_by_css_selector(self.body_input_field).send_keys(email_text)

    def click_send_btn(self):
        self.driver.find_element_by_css_selector(self.send_btn).click()

    def click_user_menu_btn(self):
        self.driver.find_element_by_css_selector(self.user_menu_btn).click()

    def click_logout_btn(self):
        self.driver.find_element_by_css_selector(self.logout_btn).click()