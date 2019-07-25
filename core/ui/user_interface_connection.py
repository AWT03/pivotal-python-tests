from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


class UserInterfaceConnection:
    def __init__(self, browser):
        self.__driver = None
        self.__browser = browser
        drivers = {
            "firefox": lambda: self.set_firefox(),
            "chrome": lambda: self.set_chrome(),
            "chrome_headless": lambda: self.set_chrome_headless()
        }
        self.__driver = drivers[browser]()

    @staticmethod
    def set_firefox():
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())

    @staticmethod
    def set_chrome():
        return webdriver.Chrome(ChromeDriverManager().install())

    @staticmethod
    def set_chrome_headless():
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    def get_driver(self):
        return self.__driver
