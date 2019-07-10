from core.ui.pages.form_page import FormPage
from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.project_main_page import ProjectMainPage

project_name_field = 'input[name="project_name"]'
account_selector_field = 'div[class="tc-account-selector"]'
account_selected = '//div[@class="tc-account-selector__option-account-name" and text()="$(name)"]'
select_private_check = 'input[data-aid="private"]'
select_public_check = 'input[data-aid="public"]'
create_button = 'button[data-aid="FormModal__submit"]'


class ProjectCreationForm(FormPage, ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "project_name": lambda value: self.set_project_name(value),
            "account": lambda value: self.set_account(value),
            "private": lambda value: self.check_private() if value else None,
            "public": lambda value: self.check_public() if value else None,
        }
        actions = {
            "Create": lambda: self.create_project()
        }
        self.update_actions(**actions)
        self.update_form_fields(**fields)

    def set_project_name(self, value):
        self.set_value(project_name_field, value)

    def set_account(self, value):
        self.click(account_selector_field)
        self.click(account_selected.replace('$(name)', value))

    def check_private(self):
        button = self.find_element(select_private_check)
        if not button.is_selected():
            button.click()

    def check_public(self):
        button = self.find_element(select_public_check)
        if not button.is_selected():
            button.click()

    def create_project(self):
        self.click(create_button)
        return ProjectMainPage(self._driver)
