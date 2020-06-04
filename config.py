import os


class Config:
    APPIUM_HOST = "http://localhost:4723/wd/hub"
    ANDROID_TODOIST_CAPS = {
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "Android Emulator",
        "automationName": "uiautomator2",
        "app": os.path.abspath('../todoist/apk/com.todoist_15.0.4-6030_minAPI21(nodpi)_apkmirror.com.apk'),
        "appPackage": "com.todoist",
        "appActivity": ".activity.HomeActivity",
      }

    TODOIST_EMAIL = ''
    TODOIST_PASSWORD = ''
    TODOIST_TOKEN = ''
