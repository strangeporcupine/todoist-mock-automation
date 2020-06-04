import time


class BasePage:

    PAGE_LOAD_WAIT = 5
    SYNC_LOAD_TIME = 15

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.PAGE_LOAD_WAIT)

    def go_back(self):
        self.driver.back()

    def wait_sync(self):
        """
        Some actions require a brief period for items to appear in todoist across both api and mobile.
        """
        # TODO: replace with explicit wait
        time.sleep(self.SYNC_LOAD_TIME)
