from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# Elements class
class Element:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 6)
        self._driver.implicitly_wait(4)

    def get_driver(self):
        return self._driver

    def set_wait(self, seconds):
        self.__wait = WebDriverWait(self._driver, seconds)

    def set_implicit_wait(self, seconds):
        self._driver.implicitly_wait(seconds)

    @staticmethod
    def get_selector(value):
        if value[:2] == '//':
            return By.XPATH
        return By.CSS_SELECTOR

    def find_element(self, value):
        return self._driver.find_element(self.get_selector(value), value)

    def find_elements(self, value):
        return self._driver.find_elements(self.get_selector(value), value)

    def add_value(self, element, value):
        self.find_element(element).send_keys(value)

    def clear_value(self, element):
        pass

    def click(self, to_click):
        self.__wait.until(ec.element_to_be_clickable((self.get_selector(to_click), to_click))).click()

    def double_click(self, to_click):
        pass

    def get_value(self, element):
        return self.find_element(element).text

    def set_value(self, element, value):
        self._driver.execute_script("arguments[0].value = ''", self.find_element(element))
        self.find_element(element).send_keys(value)

    def is_existing(self, value):
        try:
            self._driver.find_element(self.get_selector(value), value)
        except NoSuchElementException:
            return False
        return True

    def wait_for_hidden(self, *be_hidden):
        for element in be_hidden:
            self.__wait.until(ec.invisibility_of_element((self.get_selector(element), element)))

    def wait_for_visible(self, *be_shown):
        for element in be_shown:
            self.__wait.until(ec.presence_of_all_elements_located((self.get_selector(element), element)))
