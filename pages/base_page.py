from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate_to(self, url: str):
        self.driver.get(url)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def click_on(self, locator):
        self.wait_for_element(locator).click()

    def type_text(self, locator, text: str):
        self.wait_for_element(locator).send_keys(text)

