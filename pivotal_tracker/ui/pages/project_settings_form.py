from core.ui.pages.form_page import FormPage
from core.ui.pages.action_page import ActionPage


project_title_field = 'input#project_name'
description_field = 'input#project_description'
enable_task_checkbox = 'input#project_enable_tasks'
save_button = 'input.save_bar__submit'


class ProjectSettingsForm(FormPage, ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "project_title": lambda value: self.set_value(project_title_field, value),
            "description_field": lambda value: self.set_value(description_field, value),
        }
        actions = {
            "Enable Tasks": lambda: self.check_enable_tasks(),
            "Save": lambda: self.click(save_button)
        }
        self.update_actions(**actions)
        self.update_form_fields(**fields)

    def check_enable_tasks(self):
        button = self.find_element(enable_task_checkbox)
        if not button.is_selected():
            button.click()
