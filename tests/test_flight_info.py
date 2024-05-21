import pytest

from pages.select_flight_page import SelectFlightPage

@pytest.mark.select_flight
def test_select_one_way_flight(driver):
    select_flight_page = SelectFlightPage(driver)
    select_flight_page.navigate_select_flight()

    assert 'flights/start' in driver.current_url

    select_flight_page.select_trip_type('One way')
    select_flight_page.select_from_port_dropdown('Sydney')
    select_flight_page.select_to_port_dropdown('New York')
    select_flight_page.select_departing_dropdown('27', 'November 2024')
    select_flight_page.select_flight_time('8:30')
    select_flight_page.click_continue_button()

    assert 'select_date' in driver.current_url
    assert 'flights/start' not in driver.current_url

@pytest.mark.select_flight
def test_select_return_flight(driver):
    select_flight_page = SelectFlightPage(driver)
    select_flight_page.navigate_select_flight()

    assert 'flights/start' in driver.current_url

    select_flight_page.select_trip_type('Return')
    select_flight_page.select_from_port_dropdown('Sydney')
    select_flight_page.select_to_port_dropdown('New York')
    select_flight_page.select_departing_dropdown('27', 'November 2024')
    select_flight_page.select_returning_dropdown('30', 'December 2024')
    select_flight_page.select_flight_time('9:00')
    select_flight_page.click_continue_button()

    assert 'select_date' in driver.current_url
    assert 'flights/start' not in driver.current_url
