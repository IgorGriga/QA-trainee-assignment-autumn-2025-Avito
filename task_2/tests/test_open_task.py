from task_2.pages.open_task_page import OpenTaskPage


def test_open_task_success(browser):
    page = OpenTaskPage(browser)
    page.open_page()
    assert page.open_existing_task(), 'Не удалось открыть задачу'
