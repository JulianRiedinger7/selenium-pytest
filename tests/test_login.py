import pytest

from pages.login_page import LoginPage

incorrect_credentials = [
    ("", ""),
    ("agileway", ""),
    ("asd", "testwise")
]


@pytest.mark.parametrize("username, password", incorrect_credentials)
def test_incorrect_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.navigate_login()

    login_page.type_username(username)
    login_page.type_password(password)
    login_page.click_sign_in_button()

    error_message_text = login_page.get_error_message_text()
    expected_text = "Invalid email or password"

    assert error_message_text.lower() == expected_text.lower(), \
        f"Error texts are different, found: {error_message_text}"
