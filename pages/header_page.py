from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderPage(BasePage):
    WELCOME_MESSAGE = (By.ID, "user_nav")
    SIGN_OFF_BUTTON = (By.CSS_SELECTOR, "#user_nav a")

    def get_welcome_message_text(self) -> str:
        return self.wait_for_element(self.WELCOME_MESSAGE).text

    def click_sign_off_button(self):
        self.click_on(self.SIGN_OFF_BUTTON)
