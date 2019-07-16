from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 30)

    @staticmethod
    def get_selector(value):
        if value[:2] == '//':
            return By.XPATH
        else:
            return By.CSS_SELECTOR

    def find_element(self, value):
        return self._driver.find_element(self.get_selector(value), value)

    def find_elements(self, value):
        return self._driver.find_elements(self.get_selector(value), value)

    def wait_until(self, *be_hidden):
        for element in be_hidden:
            self.__wait.until(ec.invisibility_of_element((self.get_selector(element), element)))

    def click(self, to_click):
        self.__wait.until(ec.element_to_be_clickable((self.get_selector(to_click), to_click))).click()

    def set_wait(self, seconds):
        self.__wait = WebDriverWait(self._driver, seconds)

    def get_driver(self):
        return self._driver

    def mouse_hover_element(self, value):
        element = self.find_element(value)
        hover = ActionChains(self._driver).move_to_element(element)
        hover.perform()
