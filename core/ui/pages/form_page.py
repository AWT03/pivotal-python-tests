from core.ui.pages.element import Element


class FormPage(Element):
    def __init__(self, driver):
        super().__init__(driver)
        self._form_fields = {}

    def update_form_fields(self, **fields):
        for tag in fields:
            self._form_fields[tag] = fields[tag]

    def set_form(self, **setting_values):
        for tag in setting_values:
            if tag in self._form_fields:
                self._form_fields[tag](setting_values[tag])
