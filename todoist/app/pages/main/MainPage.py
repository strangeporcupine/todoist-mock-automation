from todoist.app.utils.BasePage import BasePage


class MainPage(BasePage):

    EXPAND_SIDEBAR_BUTTON = '//*[@content-desc="Change the current view"]'
    EXPAND_PROJECTS_BUTTON = '(//android.widget.RelativeLayout//*[@content-desc="Expand/collapse"])[1]'
    PROJECTS_LIST = '//android.widget.RelativeLayout[@resource-id="android:id/content"]//*[@resource-id="com.todoist:id/name"]'
    CREATE_TASK_BUTTON = 'com.todoist:id/fab'

    def expand_sidebar(self):
        self.driver.find_element_by_xpath(self.EXPAND_SIDEBAR_BUTTON).click()
        return self

    def expand_projects(self):
        self.driver.find_element_by_xpath(self.EXPAND_PROJECTS_BUTTON).click()
        return self

    def get_project_list(self):
        projects = [el.text for el in self.driver.find_elements_by_xpath(self.PROJECTS_LIST)]
        return projects

    def click_create_task_button(self):
        self.driver.find_element_by_id(self.CREATE_TASK_BUTTON).click()
        return QuickAddItemPage(self.driver)

    def open_project(self, project_name):
        self.expand_sidebar()
        self.expand_projects()
        for el in self.driver.find_elements_by_xpath(self.PROJECTS_LIST):
            if el.text == project_name:
                el.click()
                return ProjectPage(self.driver)
        raise AssertionError('Error: Project "{}" could not be found'.format(project_name))


# import at end of module to avoid circular import errors
from todoist.app.pages.main.QuickAddItemPage import QuickAddItemPage
from todoist.app.pages.main.projects.ProjectPage import ProjectPage