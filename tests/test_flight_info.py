import pytest

from pages.select_flight_page import SelectFlightPage

flight_data = [
    {
        "trip_type": "One way",
        "from_port": "Sydney",
        "to_port": "New York",
        "departing_day": "27",
        "departing_month": "November 2024",
        "flight_time": "8:30"
    },
    {
        "trip_type": "Return",
        "from_port": "San Francisco",
        "to_port": "Sydney",
        "departing_day": "15",
        "departing_month": "November 2024",
        "returnDay": "25",
        "returnMonth": "April 2025",
        "flight_time": "9:00"
    }
]


@pytest.mark.parametrize("flight", flight_data)
def test_select_one_way_flight(driver, flight):
    select_flight_page = SelectFlightPage(driver)
    select_flight_page.navigate_select_flight()

    assert 'flights/start' in driver.current_url

    select_flight_page.select_trip_type(flight.get("trip_type"))
    select_flight_page.select_from_port_dropdown(flight.get("from_port"))
    select_flight_page.select_to_port_dropdown(flight.get("to_port"))
    select_flight_page.select_departing_dropdown(flight.get("departing_day"), flight.get("departing_month"))

    if flight.get("returnDay") is not None:
        select_flight_page.select_returning_dropdown(flight.get("returnDay"), flight.get("returnMonth"))

    select_flight_page.select_flight_time(flight.get("flight_time"))
    select_flight_page.click_continue_button()

    assert 'select_date' in driver.current_url
    assert 'flights/start' not in driver.current_url
