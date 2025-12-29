from selenium.webdriver.common.by import By

from task_2.data.testcase_data import *


class Urls:
    BASE_URL = 'https://avito-tech-internship-psi.vercel.app'


class CreateTaskLocators:
    CREATE_TASK_BUTTON = (By.XPATH, '//button[text()="Создать задачу"]')
    NAME = (By.XPATH, '//input[@class="MuiInputBase-input MuiOutlinedInput-input css-1pk1fka"]')
    DESCRIPTION = (By.XPATH, '//textarea[@class="MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputMultiline css-s63k3s"]')
    PROJECTS_DROPDOWN = (By.XPATH, '//div[label[text()="Проект"]]')
    PROJECTS_NAME = (By.XPATH, f'//li[@data-value={project_name_id()}]')
    PRIORITY_DROPDOWN = (By.XPATH, '//div[label[text()="Приоритет"]]')
    PRIORITY_NAME = (By.XPATH, f'//li[@data-value="{priority_name()}"]')
    EXECUTOR_DROPDOWN = (By.XPATH, '//div[label[text()="Исполнитель"]]')
    EXECUTOR_NAME = (By.XPATH, f'//li[@data-value={executor_name_id()}]')
    CREATE_BUTTON = (By.XPATH, '//button[text()="Создать"]')


class OpenTaskLocators:
    TASK_IN_THE_TASK_LIST = (By.XPATH, '//div[@class="MuiBox-root css-69i1ev"]')
    OPEN_TASK_WINDOW = (By.XPATH, '//h5[text()="Редактирование"]')


class SearchTaskLocators:
    NAMES_TASK_FROM_TASK_LIST = (By.XPATH, '//div[@class="MuiBox-root css-69i1ev"]//h6')
    SEARCH_INPUT = (By.XPATH, '//input[@id=":r3:"]')
    SEARCH_BY_STATUS_DROPDOWN = (By.XPATH, '//div[label[text()="Статус"]]')
    STATUS_NAME = (By.XPATH, f'//li[@data-value="{status_name()}"]')
    STATUS_NAME_FROM_TASK_LIST = (By.XPATH, '//span[@class="MuiChip-label MuiChip-labelSmall css-b9zgoq"]')
    SEARCH_BY_DASHBOARD_DROPDOWN = (By.XPATH, '//div[label[text()="Доска"]]')
    DASHBOARD_NAME = (By.XPATH, f'//li[@data-value="{dashboard_name()}"]')
    DASHBOARD_NAME_FROM_TASK_LIST = (By.XPATH, '//p[@class="MuiTypography-root MuiTypography-body2 css-1xinhls"]')


class ProjectBoardLocators:
    DASHBOARD_TITTLE = (By.XPATH, '//div[@class="MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation3 css-1e90fby"]//h4')
    GO_TO_PROJECTS = (By.XPATH, '//a[text()="Проекты"]')
    TO_DASHBOARD_FROM_PROJECTS_LIST = (By.XPATH, '//a[text()="Перейти к доске"]')
