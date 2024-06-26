import allure
import pytest

from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.select_flight_page import SelectFlightPage

incorrect_credentials = [
    ("", ""),
    ("agileway", ""),
    ("asd", "testwise")
]

correct_credentials = {
    "username": "agileway",
    "password": "testwise"
}


@allure.title("Login shows an error message when trying with invalid credentials")
@allure.epic("Web UI")
@allure.feature("Login")
@allure.story("Invalid login")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("username, password", incorrect_credentials)
@pytest.mark.login
def test_invalid_login(driver, username, password):
    with allure.step("Given i navigate to the login page"):
        login_page = LoginPage(driver)
        login_page.navigate_login()

    with allure.step("When i enter invalid credentials and click on sign in button"):
        login_page.type_username(username)
        login_page.type_password(password)
        login_page.click_sign_in_button()

    with allure.step("Then i should be able to see an invalid email or password message"):
        error_message_text = login_page.get_error_message_text()
        expected_text = "Invalid email or password"

        assert error_message_text.lower() == expected_text.lower(), \
            f"Error texts are different, found: {error_message_text}"


@allure.title("Login is successful when using provided valid credentials")
@allure.epic("Web UI")
@allure.feature("Login")
@allure.story("Valid login")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.login
def test_valid_login(driver):
    with allure.step("Given i navigate to the login page"):
        login_page = LoginPage(driver)
        login_page.navigate_login()

    with allure.step("When i enter valid credentials"):
        login_page.type_username(correct_credentials["username"])
        login_page.type_password(correct_credentials["password"])
        login_page.click_sign_in_button()

    with allure.step("Then i should be able to see a successful signed in message"):
        select_flight_page = SelectFlightPage(driver)
        header_page = HeaderPage(driver)

        notice_message_text = select_flight_page.get_notice_message_text()
        welcome_message_text = header_page.get_welcome_message_text()

        expected_notice_message = "Signed in!"
        expected_welcome_message = f"Welcome {correct_credentials["username"]}"
        assert "flights" in driver.current_url, "URL did not change"

        assert notice_message_text.lower() == expected_notice_message.lower(), \
            f"Notice messages are different, found: {notice_message_text}"

        assert expected_welcome_message.lower() in welcome_message_text.lower(), \
            f"Welcome messages are different, found: {welcome_message_text}"
