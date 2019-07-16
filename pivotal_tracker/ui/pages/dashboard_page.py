from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.project_creation_form import ProjectCreationForm
from pivotal_tracker.ui.pages.project_main_page import ProjectMainPage

create_project_button = 'button[id="create-project-button"'
project_name_reference = '//a[text()="$(project_name)"]'


class DashboardPage(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "Create Project": lambda: self.open_create_project_form(),
            "Link Project Name Dashboard": lambda value: self.open_project_created_before(value),
        }
        self.update_actions(**actions)

    def open_create_project_form(self):
        self.click(create_project_button)
        return ProjectCreationForm(self._driver)

    def open_project_created_before(self, value):
        replaced = project_name_reference.replace('$(project_name)', value)
        self.click(replaced)
        return ProjectMainPage(self._driver)
