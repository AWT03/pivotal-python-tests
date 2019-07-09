from core.ui.pages.base_page import BasePage


class FormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._form_fields = {}

    def update_form_fields(self, **fields):
        for tag in fields:
            self._form_fields[tag] = fields[tag]

    def add_value(self, element, value):
        self.find_element(element).send_keys(value)

    def set_multiple(self, **setting_values):
        for tag in setting_values:
            if tag in self._form_fields:
                self._form_fields[tag](setting_values[tag])
