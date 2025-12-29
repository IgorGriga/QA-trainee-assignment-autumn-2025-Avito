import time

from task_2.pages.search_task_page import SearchTaskPage


def test_search_by_status(browser):
    page = SearchTaskPage(browser)
    page.open_page()
    page.search_by_status()
    status = page.search_by_status()
    assert status == page.first_status_from_list(), "Существующая задача не найдена через фильтр по статусу"


def test_search_by_dashboard(browser):
    page = SearchTaskPage(browser)
    page.open_page()
    page.search_by_dashboard()
    dashboard = page.search_by_dashboard()
    assert dashboard in page.first_dashboard_from_list(), "Существующая задача не найдена через фильтр по доске"


def test_search_task(browser):
    page = SearchTaskPage(browser)
    page.open_page()
    name = page.search()
    assert name == page.first_task_from_list(), "Существующая задача не найдена через поисковую строку"


def test_search_all(browser):
    test_search_by_status(browser)
    time.sleep(2)
    test_search_by_dashboard(browser)
    time.sleep(2)
    test_search_task(browser)
