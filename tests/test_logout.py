import pytest

from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.select_flight_page import SelectFlightPage


@pytest.fixture()
def login(driver):
    login_page = LoginPage(driver)
    login_page.navigate_login()
    login_page.login("agileway", "testwise")
    return login_page

def test_logout(driver, login):
    assert "start" in driver.current_url

    header_page = HeaderPage(driver)

    header_page.click_sign_off_button()

    assert "/login" in driver.current_url
    assert "Signed out!" == login.get_notice_message_text()