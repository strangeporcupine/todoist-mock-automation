from todoist.app.pages.main.MainPage import MainPage
from todoist.app.utils.BasePage import BasePage


class LoginPage(BasePage):

    LOGIN_W_EMAIL_BUTTON = 'com.todoist:id/btn_welcome_continue_with_email'
    EMAIL_TEXTBOX = 'com.todoist:id/email_exists_input'
    CONTINUE_W_EMAIL_BUTTON = 'com.todoist:id/btn_continue_with_email'
    PASSWORD_TEXTBOX = 'com.todoist:id/log_in_password'
    LOGIN_BUTTON = 'com.todoist:id/btn_log_in'

    def select_email_login(self):
        self.driver.find_element_by_id(self.LOGIN_W_EMAIL_BUTTON).click()
        return self

    def set_email(self, email):
        self.driver.find_element_by_id(self.EMAIL_TEXTBOX).send_keys(email)
        return self

    def continue_with_email(self):
        self.driver.find_element_by_id(self.CONTINUE_W_EMAIL_BUTTON).click()
        return self

    def set_password(self, password):
        self.driver.find_element_by_id(self.PASSWORD_TEXTBOX).send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element_by_id(self.LOGIN_BUTTON).click()
        return MainPage(self.driver)
