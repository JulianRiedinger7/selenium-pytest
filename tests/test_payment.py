import allure
import pytest

from pages.details_page import DetailsPage
from pages.payment_page import PaymentPage
from pages.select_flight_page import SelectFlightPage
from utils.functions import transform_date


@pytest.fixture()
def flight_details(driver):
    flight_data = {
        "trip_type": "One way",
        "from_port": "Sydney",
        "to_port": "New York",
        "departing_day": "27",
        "departing_month": "November 2024",
        "flight_time": "8:30"
    }
    select_flight_page = SelectFlightPage(driver)
    select_flight_page.navigate_select_flight()
    select_flight_page.select_trip_type(flight_data.get("trip_type"))
    select_flight_page.select_from_port_dropdown(flight_data.get("from_port"))
    select_flight_page.select_to_port_dropdown(flight_data.get("to_port"))
    select_flight_page.select_departing_dropdown(flight_data.get("departing_day"), flight_data.get("departing_month"))
    select_flight_page.select_flight_time(flight_data.get("flight_time"))
    select_flight_page.click_continue_button()

    return flight_data

@allure.title("Payment and passenger details are the same as flight selection")
@allure.epic("Web UI")
@allure.feature("Payment")
@allure.story("Valid payments details")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.payment
def test_payment(driver, flight_details):
    passenger_info = {
        "first_name": "Julian",
        "last_name": "Perez",
        "card_type": "Master",
        "card_number": "123123",
        "expiry_month": "07",
        "expiry_year": "2027"
    }

    with allure.step("Given i am on the details page"):
        details_page = DetailsPage(driver)

    with allure.step("When i enter the passenger name and credit card and click on pay now button"):
        details_page.type_first_name(passenger_info.get("first_name"))
        details_page.type_last_name(passenger_info.get("last_name"))
        details_page.click_next_button()

        assert "flights/passenger" in driver.current_url

        payment_page = PaymentPage(driver)

        fare_details = payment_page.get_fare_details_text()
        expected_fare_details = f"{flight_details.get("trip_type").lower().replace(" ", "")} {flight_details.get("from_port")} to {flight_details.get("to_port")}"
        card_holder_value = payment_page.get_holder_name_input_value()
        passenger_full_name = f"{passenger_info.get("first_name")} {passenger_info.get("last_name")}"

        assert expected_fare_details == fare_details, f"Incorrect fare details: found {fare_details}"
        assert passenger_full_name == card_holder_value, f"Incorrect card holder, found {card_holder_value}"

        payment_page.select_card_type(passenger_info.get("card_type"))
        payment_page.type_card_number(passenger_info.get("card_number"))
        payment_page.select_expiry(passenger_info.get("expiry_month"), passenger_info.get("expiry_year"))
        payment_page.click_pay_now_button()

    with allure.step("Then i should be able to see the corresponding confirmation details"):
        confirmation_details = payment_page.get_confirmation_details_text()
        transformed_departing_date = transform_date(
            f"{flight_details.get("departing_day")} {flight_details.get("departing_month")}")

        assert flight_details.get("trip_type").lower().replace(" ", "") in confirmation_details
        assert (f"{transformed_departing_date} {flight_details.get("from_port")} to {flight_details.get("to_port")}"
                in confirmation_details)
        assert passenger_full_name in payment_page.get_passenger_details_text(), "Full name incorrect"
