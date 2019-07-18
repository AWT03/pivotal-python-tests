from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from pivotal_tracker.ui.pages.tabs.user_main_tabs import UserMainTabs
from pivotal_tracker.ui.pages.tabs.dashboard_tabs import DashboardTabs
from selenium.common.exceptions import NoSuchElementException

create_project_button = 'button[id="create-project-button"'
project_name_reference = '//a[text()="$(project_name)"]'


class DashboardProjects(ActionPage, FormPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "Create Project": lambda: self.open_create_project_form()
        }
        self.update_actions(**actions)

    def open_create_project_form(self):
        self.click(create_project_button)
        return UserMainTabs.PROJECT_CREATION

    def project_exists(self, name):
        try:
            self.find_element(project_name_reference.replace('$(project_name)', name))
            return True
        except NoSuchElementException:
            return False
