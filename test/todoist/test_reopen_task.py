import pytest

from todoist.app.pages.LoginPage import LoginPage


@pytest.mark.stable
def test_reopen_task(driver, todoist_api, todoist_test_user):
    TEST_TASK_NAME = 'test_task_reopen'
    TEST_PROJECT_NAME = 'test_task_reopen_project'

    # Create project via API
    resp = todoist_api.create_project(TEST_PROJECT_NAME)
    project_id = resp['id']

    # Login to Todoist
    login_page = LoginPage(driver)
    main_page = login_page.select_email_login() \
        .set_email(todoist_test_user['email']) \
        .continue_with_email() \
        .set_password(todoist_test_user['password']) \
        .click_login()

    # Create task via Mobile
    project_page = main_page.open_project(TEST_PROJECT_NAME)
    project_page.click_create_task_button()\
        .add_task(TEST_TASK_NAME)

    # Get Tasks via api before task complete
    tasks = todoist_api.get_tasks_by_project(project_id)
    task_details = None
    for t in tasks:
        if t['content'] == TEST_TASK_NAME:
            task_details = t

    assert task_details, 'Task "{}" was not found in project "{}"'.format(TEST_TASK_NAME, TEST_PROJECT_NAME)

    # Complete Task
    project_page.open_task(TEST_TASK_NAME)\
        .complete_task()

    # Reopen task via API
    todoist_api.reopen_task(task_details['id'])

    # Get Tasks via api after reopen task
    tasks_2 = todoist_api.get_tasks_by_project(project_id)

    assert TEST_TASK_NAME in [t['content'] for t in tasks_2]
