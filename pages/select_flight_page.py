from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SelectFlightPage(BasePage):
    NOTICE_MESSAGE = (By.ID, "flash_notice")
    FROM_DROPDOWN = (By.NAME, "fromPort")
    TO_DROPDOWN = (By.NAME, "toPort")
    DEPART_DAY_DROPDOWN = (By.ID, "departDay")
    DEPART_MONTH_DROPDOWN = (By.ID, "departMonth")
    RETURN_DAY_DROPDOWN = (By.ID, "returnDay")
    RETURN_MONTH_DROPDOWN = (By.ID, "returnMonth")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type = 'submit']")

    def navigate_select_flight(self):
        self.navigate_to("https://travel.agileway.net/flights/start")

    def get_notice_message_text(self) -> str:
        return self.wait_for_element(self.NOTICE_MESSAGE).text

    def select_trip_type(self, option: str):
        formatted_option = option.strip().lower().replace(' ', '')

        assert formatted_option in ['return', 'oneway'], "Option must be Return or One Way"

        radio_button_locator = (
            By.XPATH,
            f"//input[@type = 'radio' and @value='{formatted_option}']"
        )

        self.select_element(radio_button_locator)

    def select_from_port_dropdown(self, option: str):
        available_options = self.get_dropdown_options(self.FROM_DROPDOWN)

        assert option in available_options, f"Option must be some of {available_options}"

        self.select_from_dropdown_by_visible_text(self.FROM_DROPDOWN, option)


    def select_to_port_dropdown(self, option: str):
        available_options = self.get_dropdown_options(self.TO_DROPDOWN)

        assert option in available_options, f"Option must be some of {available_options}"

        self.select_from_dropdown_by_visible_text(self.TO_DROPDOWN, option)


    def select_departing_dropdown(self, day: str, month: str):
        available_days = self.get_dropdown_options(self.DEPART_DAY_DROPDOWN)
        available_months = self.get_dropdown_options(self.DEPART_MONTH_DROPDOWN)

        assert day in available_days, f"Day must be some of {available_days}"
        assert month in available_months, f"Day must be some of {available_months}"

        self.select_from_dropdown_by_visible_text(self.DEPART_DAY_DROPDOWN, day)
        self.select_from_dropdown_by_visible_text(self.DEPART_MONTH_DROPDOWN, month)


    def select_returning_dropdown(self, day: str, month: str):
        available_days = self.get_dropdown_options(self.RETURN_DAY_DROPDOWN)
        available_months = self.get_dropdown_options(self.RETURN_MONTH_DROPDOWN)

        assert day in available_days, f"Day must be some of {available_days}"
        assert month in available_months, f"Day must be some of {available_months}"

        self.select_from_dropdown_by_visible_text(self.RETURN_DAY_DROPDOWN, day)
        self.select_from_dropdown_by_visible_text(self.RETURN_MONTH_DROPDOWN, month)


    def select_flight_time(self, time: str):
        checkbox_locator = (
            By.XPATH,
            f"//td[contains(., '{time}')]/parent::tr/th/input[@type = 'checkbox']"
        )

        self.select_element(checkbox_locator)

    def click_continue_button(self):
        self.click_on(self.CONTINUE_BUTTON)

