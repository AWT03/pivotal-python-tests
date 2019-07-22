from core.ui.pages.action_page import ActionPage
from core.ui.pages.element_search import ElementSearch
from pivotal_tracker.ui.pages.tabs.user_main_tabs import UserMainTabs

create_project_button = 'button[id="create-project-button"'
project_name_reference = '//a[text()="$(project_name)"]'


class DashboardProjects(ActionPage, ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        search_elements = {
            "projects_dashboard": lambda value: self.project_exists(value)
        }
        actions = {
            "Create Project": lambda: self.open_create_project_form()
        }
        self.update_actions(**actions)
        self.update_search_fields(**search_elements)

    def open_create_project_form(self):
        self.click(create_project_button)
        return UserMainTabs.PROJECT_CREATION

    def project_exists(self, name):
        return self.is_existing(project_name_reference.replace('$(project_name)', name))
