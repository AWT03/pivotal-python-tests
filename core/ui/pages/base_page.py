from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self._driver = driver

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

    def click(self, to_click, *be_hidden):
        wait = WebDriverWait(self._driver, 30)
        for element in be_hidden:
            wait.until(ec.invisibility_of_element((self.get_selector(element), element)))
        wait.until(ec.element_to_be_clickable((self.get_selector(to_click), to_click))).click()
