from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SelectFlightPage(BasePage):
    NOTICE_MESSAGE = (By.ID, "flash_notice")

    def get_notice_message_text(self) -> str:
        return self.wait_for_element(self.NOTICE_MESSAGE).text


