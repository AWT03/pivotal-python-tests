from core.ui.pages.form_page import FormPage
from core.ui.pages.action_page import ActionPage


project_title_field = 'input#project_name'
description_field = 'input#project_description'
enable_task_checkbox = 'input#project_enable_tasks'
save_button = 'input.save_bar__submit'
stories_tab = 'a[data-aid*="navTab-stories"]'
analytics_tab = 'a[data-aid*="navTab-analytics"]'
context_name = 'span.raw_context_name'


class ProjectSettingsForm(FormPage, ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "project_title": lambda value: self.set_value(project_title_field, value),
            "description_field": lambda value: self.set_value(description_field, value),
            "Enable Tasks": lambda value: self.check_enable_tasks() if value else None,
            "Save": lambda value: self.save_changes() if value else None
        }
        actions = {
            "Stories Tab": lambda: self.click(stories_tab),
            "Analytics tab": lambda: self.click(analytics_tab),
        }
        self.update_actions(**actions)
        self.update_form_fields(**fields)

    def check_enable_tasks(self):
        button = self.find_element(enable_task_checkbox)
        if button.is_selected():
            button.click()

    def save_changes(self):
        self.click(save_button)
        self._driver.switch_to.alert.accept()


