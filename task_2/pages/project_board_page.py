from task_2.base.base_page import BasePage
from task_2.base.locators import Urls
from task_2.base.locators import ProjectBoardLocators as PBL


class ProjectBoardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        self.driver.get(Urls.BASE_URL)

    def get_dashboard_tittle(self):
        return self.is_visible(PBL.DASHBOARD_TITTLE).text

    def go_to_projects(self):
        self.click_on_el(PBL.GO_TO_PROJECTS)

    def go_to_dashboard_from_project_list(self):
        self.click_on_el(PBL.TO_DASHBOARD_FROM_PROJECTS_LIST)

    def dashboard(self, tittle):
        list = ["Редизайн карточки товара",
                "Все",
                "Оптимизация производительности",
                "Рефакторинг API",
                "Миграция на новую БД",
                "Автоматизация тестирования",
                "Переход на Kubernetes"]
        if tittle in list:
            return True
        else:
            return False
