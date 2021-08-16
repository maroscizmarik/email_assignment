import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.loginPage import LoginPage
from Pages.emailPage import EmailPage
from config.config import URL, USERNAME, PASSWORD, RECIPIENT_NAME


class EmailTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_send_email(self):
        driver = self.driver
        driver.get(URL)

        login = LoginPage(driver)
        login.enter_username(USERNAME)
        login.click_btn_next()
        login.enter_password(PASSWORD)
        login.click_login_btn()

        email = EmailPage(driver)
        email.click_compose_btn()
        email.enter_recipient(RECIPIENT_NAME)
        email.enter_subject("Hello")
        email.enter_email_text("Test")
        email.click_send_btn()
        time.sleep(5)

        email.click_user_menu_btn()
        email.click_logout_btn()

        time.sleep(5)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
