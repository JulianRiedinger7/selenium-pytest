import allure
import pytest

from pages.details_page import DetailsPage
from pages.select_flight_page import SelectFlightPage
from utils.functions import transform_date

flight_data = [
    {
        "trip_type": "Return",
        "from_port": "San Francisco",
        "to_port": "Sydney",
        "departing_day": "15",
        "departing_month": "November 2024",
        "return_day": "25",
        "return_month": "April 2025",
        "flight_time": "9:00"
    },
    {
        "trip_type": "One way",
        "from_port": "Sydney",
        "to_port": "New York",
        "departing_day": "27",
        "departing_month": "November 2024",
        "flight_time": "8:30"
    }
]


@allure.title("Flight details show up correctly when selecting different trip types")
@allure.epic("Web UI")
@allure.feature("Flight selection")
@allure.story("Valid flight details")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.flight_selection
@pytest.mark.parametrize("flight", flight_data)
def test_select_flight(driver, flight):
    with allure.step("Given i navigate to the select flight page"):
        select_flight_page = SelectFlightPage(driver)
        select_flight_page.navigate_select_flight()

        assert 'flights/start' in driver.current_url

    with allure.step("When i enter the flight information and click on continue button"):
        select_flight_page.select_trip_type(flight.get("trip_type"))
        select_flight_page.select_from_port_dropdown(flight.get("from_port"))
        select_flight_page.select_to_port_dropdown(flight.get("to_port"))
        select_flight_page.select_departing_dropdown(flight.get("departing_day"), flight.get("departing_month"))

        if flight.get("return_day") is not None:
            select_flight_page.select_returning_dropdown(flight.get("return_day"), flight.get("return_month"))

        select_flight_page.select_flight_time(flight.get("flight_time"))
        select_flight_page.click_continue_button()

    with allure.step("Then i should be able to see the details page with the corresponding flight information"):
        assert 'select_date' in driver.current_url
        assert 'flights/start' not in driver.current_url

        details_page = DetailsPage(driver)

        flight_details = details_page.get_flight_details_text()
        transformed_departing_date = transform_date(f"{flight.get("departing_day")} {flight.get("departing_month")}")

        if flight.get("return_day") is not None:
            transformed_return_date = transform_date(f"{flight.get("return_day")} {flight.get("return_month")}")

            assert flight.get("trip_type").lower() in flight_details, "Trip type was not found"
            assert transformed_return_date in flight_details, "Return date was not found"
            assert f"{flight.get("to_port")} to {flight.get("from_port")}" in flight_details, (
                "Destination to Origin was "
                "not found")
        else:
            assert flight.get("trip_type").lower().replace(" ", "") in flight_details, "Trip type was not found"

        assert transformed_departing_date in flight_details, "Departing date was not found"
        assert f"{flight.get("from_port")} to {flight.get("to_port")}" in flight_details, ("Origin to Destination was "
                                                                                           "not found")
