from todoist.app.pages.main.MainPage import MainPage
from todoist.app.utils.BasePage import BasePage


class TaskQuickAddPage(BasePage):

    TASK_NAME_TEXTBOX = 'android:id/message'
    ADD_TASK_BUTTON = 'android:id/button1'

    def set_task_name(self, task_name):
        self.driver.find_element_by_id(self.TASK_NAME_TEXTBOX).send_keys(task_name)
        return self

    def add_task(self, task_name):
        self.set_task_name(task_name)
        self.driver.find_element_by_id(self.ADD_TASK_BUTTON).click()
        self.wait_sync()
        self.go_back()
        return MainPage(self.driver)
