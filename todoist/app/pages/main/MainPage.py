from todoist.app.utils.BasePage import BasePage


class MainPage(BasePage):

    EXPAND_SIDEBAR_BUTTON = '//*[@content-desc="Change the current view"]'
    EXPAND_PROJECTS_BUTTON = '(//android.widget.RelativeLayout//*[@content-desc="Expand/collapse"])[1]'
    PROJECTS_LIST = '//android.widget.RelativeLayout[@resource-id="android:id/content"]//*[@resource-id="com.todoist:id/name"]'

    def expand_sidebar(self):
        self.driver.find_element_by_xpath(self.EXPAND_SIDEBAR_BUTTON).click()
        return self

    def expand_projects(self):
        self.driver.find_element_by_xpath(self.EXPAND_PROJECTS_BUTTON).click()
        return self

    def get_project_list(self):
        projects = [el.text for el in self.driver.find_elements_by_xpath(self.PROJECTS_LIST)]
        return projects
