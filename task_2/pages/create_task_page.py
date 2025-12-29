from task_2.base.base_page import BasePage
from task_2.base.locators import Urls
from task_2.base.locators import CreateTaskLocators as CTL
from task_2.data.testcase_data import *


class CreateTaskPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        self.driver.get(Urls.BASE_URL)

    def click_create_task_button(self):
        self.click_on_el(CTL.CREATE_TASK_BUTTON)

    def fill_task_name(self):
        name = task_name()
        self.fill_field(CTL.NAME, name)

    def fill_task_description(self):
        description = task_description()
        self.fill_field(CTL.DESCRIPTION, description)

    def select_project(self):
        self.click_on_el(CTL.PROJECTS_DROPDOWN)
        self.click_on_el(CTL.PROJECTS_NAME)

    def select_priority(self):
        self.click_on_el(CTL.PRIORITY_DROPDOWN)
        self.click_on_el(CTL.PRIORITY_NAME)

    def select_executor(self):
        self.click_on_el(CTL.EXECUTOR_DROPDOWN)
        self.click_on_el(CTL.EXECUTOR_NAME)

    def click_create_button(self):
        self.click_on_el(CTL.CREATE_BUTTON)
        return True
