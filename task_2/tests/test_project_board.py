import time

from task_2.pages.project_board_page import ProjectBoardPage


def test_project_board_success(browser):
    page = ProjectBoardPage(browser)
    page.open_page()
    page.go_to_projects()
    page.go_to_dashboard_from_project_list()
    tittle = page.get_dashboard_tittle()
    assert page.dashboard(tittle), 'Не удалось перейти на доску'
    time.sleep(2)
