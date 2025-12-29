from task_2.pages.create_task_page import CreateTaskPage


def test_create_task_success(browser):
    page = CreateTaskPage(browser)
    page.open_page()
    page.click_create_task_button()
    page.fill_task_name()
    page.fill_task_description()
    page.select_project()
    page.select_priority()
    page.select_executor()
    assert page.click_create_button(), 'Не удалось создать задачу'
