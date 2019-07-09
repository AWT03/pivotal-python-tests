from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class UserInterfaceConnection:
    def __init__(self, browser=None):
        self.__driver = None
        self.__browser = None
        self.set_browser(browser)

    def set_browser(self, browser):
        self.__browser = browser
        if browser.lower() == 'firefox':
            self.__driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser.lower() == 'chrome':
            self.__driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            self.__driver = None

    def get_driver(self):
        return self.__driver
