from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SIGN_IN_BUTTON = (By.NAME, "commit")
    ERROR_MESSAGE = (By.ID, "flash_alert")
    REMEMBER_ME_CHECKBOX = (By.ID, "remember_me")
    NOTICE_MESSAGE = (By.ID, "flash_notice")

    def navigate_login(self):
        self.navigate_to("https://travel.agileway.net/")

    def type_username(self, username: str):
        self.type_text(self.USERNAME_INPUT, username)

    def type_password(self, password: str):
        self.type_text(self.PASSWORD_INPUT, password)

    def click_sign_in_button(self):
        self.click_on(self.SIGN_IN_BUTTON)

    def get_error_message_text(self) -> str:
        return self.wait_for_element(self.ERROR_MESSAGE).text

    def select_remember_me_checkbox(self):
        self.select_element(self.REMEMBER_ME_CHECKBOX)

    def login(self, username: str, password: str):
        self.type_username(username)
        self.type_password(password)
        self.select_remember_me_checkbox()
        self.click_sign_in_button()

    def get_notice_message_text(self) -> str:
        return self.wait_for_element(self.NOTICE_MESSAGE).text
