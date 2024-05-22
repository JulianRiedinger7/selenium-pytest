from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DetailsPage(BasePage):
    FLIGHT_DETAILS = (By.XPATH, "//div[@id = 'container']/div[2]")
    FIRST_NAME_INPUT = (By.NAME, "passengerFirstName")
    LAST_NAME_INPUT = (By.NAME, "passengerLastName")
    NEXT_BUTTON = (By.CSS_SELECTOR, "input[value = 'Next']")

    def get_flight_details_text(self) -> str:
        return self.wait_for_element(self.FLIGHT_DETAILS).text


    def type_first_name(self, first_name: str):
        self.type_text(self.FIRST_NAME_INPUT, first_name)


    def type_last_name(self, last_name: str):
        self.type_text(self.LAST_NAME_INPUT, last_name)


    def click_next_button(self):
        self.click_on(self.NEXT_BUTTON)

