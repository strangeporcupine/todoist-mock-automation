import pytest
from appium import webdriver

from config import Config
from todoist.api.client import TodoistAPI


@pytest.fixture
def config():
    return Config()


@pytest.fixture
def driver(config):
    driver = webdriver.Remote(config.APPIUM_HOST, config.ANDROID_TODOIST_CAPS)
    yield driver
    driver.quit()


@pytest.fixture
def todoist_api(config):
    if not config.TODOIST_TOKEN:
        pytest.fail('Unable to find valid Todoist API Token in config file')
    api = TodoistAPI(config.TODOIST_TOKEN)
    yield api


@pytest.fixture
def todoist_test_user(config):
    if not (config.TODOIST_EMAIL and config.TODOIST_PASSWORD):
        pytest.fail('Incomplete credentials. Kindly add Todoist credentials to config.py file.')
    credentials = {'email': config.TODOIST_EMAIL, 'password': config.TODOIST_PASSWORD}
    return credentials
