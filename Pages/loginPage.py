from Locators.loginPageLocators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_input_field = Locators.username_input_field_id
        self.next_btn = Locators.next_btn_id
        self.password_input_field = Locators.password_input_field_name
        self.login_btn = Locators.login_btn_id

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_input_field).send_keys(username)

    def click_btn_next(self):
        self.driver.find_element_by_id(self.next_btn).click()

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_input_field).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element_by_id(self.login_btn).click()
