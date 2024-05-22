from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PaymentPage(BasePage):
    FARE_DETAILS = (By.CSS_SELECTOR, "div i")
    HOLDER_NAME_INPUT = (By.NAME, "holder_name")
    CARD_NUMBER_INPUT = (By.NAME, "card_number")
    EXPIRY_MONTH_DROPDOWN = (By.NAME, "expiry_month")
    EXPIRY_YEAR_DROPDOWN = (By.NAME, "expiry_year")
    PAY_NOW_BUTTON = (By.CSS_SELECTOR, "input[value = 'Pay now']")
    CONFIRMATION_DETAILS = (By.CSS_SELECTOR, "#confirmation div")
    PASSENGER_DETAILS = (By.CSS_SELECTOR, "#confirmation p:last-child")

    def get_fare_details_text(self) -> str:
        return self.wait_for_element(self.FARE_DETAILS).text

    def get_holder_name_input_value(self) -> str:
        return self.wait_for_element(self.HOLDER_NAME_INPUT).get_attribute("value")

    def type_card_number(self, number: str):
        self.type_text(self.CARD_NUMBER_INPUT, number)

    def select_card_type(self, card_type: str):
        assert card_type.lower() in ["visa", "master"], "Card type must be Visa or Master"

        card_type_selector = (
            By.XPATH,
            f"//input[@name = 'card_type' and @value = '{card_type.lower()}']"
        )

        self.select_element(card_type_selector)

    def select_expiry(self, month: str, year: str):
        available_months = self.get_dropdown_options(self.EXPIRY_MONTH_DROPDOWN)
        available_years = self.get_dropdown_options(self.EXPIRY_YEAR_DROPDOWN)

        assert month in available_months, f"{month} must be some of {available_months}"
        assert year in available_years, f"{year} must be some of {available_years}"

        self.select_from_dropdown_by_visible_text(self.EXPIRY_MONTH_DROPDOWN, month)
        self.select_from_dropdown_by_visible_text(self.EXPIRY_YEAR_DROPDOWN, year)

    def click_pay_now_button(self):
        self.click_on(self.PAY_NOW_BUTTON)

    def get_confirmation_details_text(self) -> str:
        return self.wait_for_element(self.CONFIRMATION_DETAILS).text

    def get_passenger_details_text(self) -> str:
        return self.wait_for_element(self.PASSENGER_DETAILS).text
