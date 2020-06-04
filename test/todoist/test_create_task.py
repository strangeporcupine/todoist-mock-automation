import pytest

from todoist.app.pages.LoginPage import LoginPage

@pytest.mark.stable
def test_create_task(driver, todoist_api, todoist_test_user):
    TEST_TASK_NAME = 'test_task_creation'
    TEST_PROJECT_NAME = 'test_task_project'

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
    main_page.open_project(TEST_PROJECT_NAME)\
        .click_create_task_button()\
        .add_task(TEST_TASK_NAME)

    # Get task via API
    tasks = todoist_api.get_tasks_by_project(project_id)

    assert TEST_TASK_NAME in [t['content'] for t in tasks]

    # Cleanup
    todoist_api.delete_project_by_name(TEST_PROJECT_NAME)
