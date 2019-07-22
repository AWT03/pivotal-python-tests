from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from selenium.common.exceptions import NoSuchElementException

project_title_field = 'input[name="project[name]"][value="$(name)"]'
project_account_label = '//span[@id="project_account"]/b[contains(text(), $(name))]'
privacy_checked = 'input[name="project[public]"]'
enable_tasks_checked = 'input#project_enable_tasks'
description_field = 'input#project_description'

field_map = {
    "project_name": project_title_field,
    "account": project_account_label,
    "privacy": privacy_checked
}


class ProjectMore(ActionPage, FormPage):
    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            # "project_title": lambda value: self.set_value(project_title_field, value),
            "description_field": lambda value: self.set_value(description_field, value),
            "Enable Tasks": lambda value: self.check_enable_tasks(value)
        }
        actions = {
            # "Stories Tab": lambda: self.click(stories_tab),
            # "Analytics tab": lambda: self.click(analytics_tab),
            "Save": lambda value: self.save_changes()
        }
        self.update_actions(**actions)
        self.update_form_fields(**fields)

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

    def check_enable_tasks(self, value):
        button = self.find_element(enable_tasks_checked)
        if button.is_selected() != value:
            button.click()

    def save_changes(self):
        self.click(save_button)
        self._driver.switch_to.alert.accept()
