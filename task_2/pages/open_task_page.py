from task_2.base.base_page import BasePage
from task_2.base.locators import Urls
from task_2.base.locators import OpenTaskLocators as OTL


class OpenTaskPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        self.driver.get(Urls.BASE_URL)

    def open_existing_task(self):
        self.click_on_el(OTL.TASK_IN_THE_TASK_LIST)
        self.is_visible(OTL.OPEN_TASK_WINDOW)
        return True
