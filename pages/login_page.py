from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username"),
    PASSWORD_INPUT = (By.ID, "password"),
    SIGN_IN_BUTTON = (By.NAME, "commit")


    def navigate_login(self, url: str):
        self.navigate_to(url)


    def type_username(self, username: str):
        self.type_text(self.USERNAME_INPUT, username)


    def type_password(self, password: str):
        self.type_text(self.PASSWORD_INPUT, password)


    def click_sign_in_button(self):
        self.click_on(self.SIGN_IN_BUTTON)

