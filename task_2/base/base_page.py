from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator), message='Элемент не отобразилсся на странице')

    def is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator), message='Не удалось дождаться кликабельности элемента')

    def fill_field(self, locator, text):
        self.is_visible(locator).send_keys(text)

    def click_on_el(self, locator):
        self.is_clickable(locator).click()
