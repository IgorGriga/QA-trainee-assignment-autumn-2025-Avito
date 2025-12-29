from task_2.base.base_page import BasePage
from task_2.base.locators import Urls
from task_2.base.locators import SearchTaskLocators as STL


class SearchTaskPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        self.driver.get(Urls.BASE_URL)

    def search_by_status(self):
        self.click_on_el(STL.SEARCH_BY_STATUS_DROPDOWN)
        status = self.is_visible(STL.STATUS_NAME)
        status.click()
        status = status.text
        return status

    def first_status_from_list(self):
        return self.is_visible(STL.STATUS_NAME_FROM_TASK_LIST).text

    def search_by_dashboard(self):
        self.click_on_el(STL.SEARCH_BY_DASHBOARD_DROPDOWN)
        dashboard = self.is_visible(STL.DASHBOARD_NAME)
        dashboard.click()
        dashboard = dashboard.text
        return dashboard

    def first_dashboard_from_list(self):
        return self.is_visible(STL.DASHBOARD_NAME_FROM_TASK_LIST).text

    def search(self):
        names = self.is_visible(STL.NAMES_TASK_FROM_TASK_LIST)
        name = names.text
        self.fill_field(STL.SEARCH_INPUT, name)
        return name

    def first_task_from_list(self):
        names = self.is_visible(STL.NAMES_TASK_FROM_TASK_LIST)
        name = names.text
        return name
