from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HeaderPage(BasePage):
    WELCOME_MESSAGE = (By.ID, "user_nav")


    def get_welcome_message_text(self) -> str:
        return self.wait_for_element(self.WELCOME_MESSAGE).text

