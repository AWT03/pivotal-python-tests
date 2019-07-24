from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from selenium.common.exceptions import NoSuchElementException
from core.ui.pages.element_search import ElementSearch

workspace_title_field = 'input[class="settings_field"][value=$(name)]'
header_name_more = '//div[text()="$(expected_name)"]'

field_map = {
    "workspace_name": workspace_title_field
}


class WorkspaceMore(ActionPage, FormPage, ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        self._search_elements = {
            "header_name_more": lambda value: self.validate_header_name_more(value)
        }
        fields = {
            "workspace_title": lambda value: self.set_value(workspace_title_field, value)
        }
        self.update_form_fields(**fields)

    def match_fields(self, **values):
        for tag in values:
            try:
                field_ref = field_map[tag]
                fsf = field_ref.replace('$(name)', values[tag])
                self.find_element(field_ref.replace('$(name)', values[tag]))
            except NoSuchElementException:
                return False
        return True

    def validate_header_name_more(self, name):
        return self.is_existing(header_name_more.replace('$(expected_name)', name))
