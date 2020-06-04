from todoist.app.pages.main.projects.ProjectPage import ProjectPage
from todoist.app.utils.BasePage import BasePage


class TaskScrollViewPage(BasePage):

    COMPLETE_BUTTON = 'com.todoist:id/item_checkmark'

    def complete_task(self):
        self.driver.find_element_by_id(self.COMPLETE_BUTTON).click()
        return ProjectPage(self.driver)
