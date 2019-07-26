from core.ui.pages.element import Element


class ElementSearch(Element):
    def __init__(self, driver):
        super().__init__(driver)
        self._search_elements = {}

    def update_search_fields(self, **fields):
        for tag in fields:
            self._search_elements[tag] = fields[tag]

    def is_displayed_as(self, key, *values):
        return self._search_elements[key](*values)
