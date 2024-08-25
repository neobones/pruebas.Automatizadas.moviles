from appium import webdriver
from browserstack_sdk import BrowserStackLocal
from config.browserstack_config import BROWSERSTACK_CONFIG
from config.local_config import LOCAL_CONFIG

class DriverFactory:
    @staticmethod
    def get_driver(use_browserstack=False):
        if use_browserstack:
            return DriverFactory._get_browserstack_driver()
        else:
            return DriverFactory._get_local_driver()

    @staticmethod
    def _get_browserstack_driver():
        return webdriver.Remote(
            command_executor="http://hub-cloud.browserstack.com/wd/hub",
            desired_capabilities=BROWSERSTACK_CONFIG
        )

    @staticmethod
    def _get_local_driver():
        return webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities=LOCAL_CONFIG
        )