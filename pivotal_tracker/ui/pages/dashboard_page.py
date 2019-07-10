from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.project_creation_form import ProjectCreationForm

create_project_button = 'button[id="create-project-button"'


class DashboardPage(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "Create Project": lambda: self.open_create_project_form()
        }
        self.update_actions(**actions)

    def open_create_project_form(self):
        self.click(create_project_button)
        return ProjectCreationForm(self._driver)
