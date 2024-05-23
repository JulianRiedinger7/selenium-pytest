import allure
import pytest

from pages.header_page import HeaderPage
from pages.login_page import LoginPage

@pytest.fixture()
def login(driver):
    login_page = LoginPage(driver)
    login_page.navigate_login()
    login_page.login("agileway", "testwise")
    return login_page

@allure.title("Logout successful message appears after sign off")
@allure.epic("Web UI")
@allure.feature("Logout")
@allure.story("Valid logout")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.logout
def test_logout(driver, login):
    with allure.step("Given i am already logged in"):
        assert "start" in driver.current_url

    with allure.step("When i click on the sign off button"):
        header_page = HeaderPage(driver)

        header_page.click_sign_off_button()

    with allure.step("Then i should be able to see a successful signed out message"):
        assert "/login" in driver.current_url
        assert "Signed out!" == login.get_notice_message_text()