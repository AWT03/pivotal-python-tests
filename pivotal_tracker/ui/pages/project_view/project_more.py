from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from selenium.common.exceptions import NoSuchElementException

project_title_field = 'input[name="project[name]"][value="$(name)"]'
project_account_label = '//span[@id="project_account"]/b[contains(text(), "$(name)")]'
privacy_checked = 'input[name="project[public]"]'

field_map = {
    "project_name": project_title_field,
    "account": project_account_label,
    "privacy": privacy_checked
}


class ProjectMore(ActionPage, FormPage):
    def __init__(self, driver):
        super().__init__(driver)

    def match_fields(self, **values):
        for tag in values:
            try:
                field_ref = field_map[tag]
                if tag == "privacy" and values[tag] == "private":
                    field_ref += '[checked="checked"]'
                self.find_element(field_ref.replace('$(name)', values[tag]))
            except NoSuchElementException:
                return False
        return True
