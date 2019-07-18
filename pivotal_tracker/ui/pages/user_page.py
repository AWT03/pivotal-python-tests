from core.ui.pages.tab_page import TabPage
from pivotal_tracker.ui.pages.dashboard.dashboard_page import DashboardPage
from pivotal_tracker.ui.pages.project_view.project_main import ProjectMain
from pivotal_tracker.ui.pages.project_view.projects_all import ProjectAll
from pivotal_tracker.ui.pages.pop_ups.project_creation_form import ProjectCreationForm
from selenium.common.exceptions import NoSuchElementException

go_dashboard_button = '.headerLogo__image'
page_name = '//span[text()="$(expected_name)"]'
projects_dropdown_list = '.tc_projects_dropdown_link.tc_context_name'
show_all_projects_button = '//span[text()="Show All Projects"]'


class UserPage(TabPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._tabs = {
            "Dashboard": lambda: self.get_dashboard_tab(),
            "ProjectMain": lambda: self.get_project_main_tab(),
            "AllProjects": lambda: self.get_all_projects(),
            "ProjectCreation": lambda: self.get_project_creation_form()
        }
        self._tab = DashboardPage(self._driver)

    def get_dashboard_tab(self):
        self.click(go_dashboard_button)
        self._tab = DashboardPage(self._driver)

    def get_project_main_tab(self):
        self._tab = ProjectMain(self._driver)

    def get_all_projects(self):
        self.click(projects_dropdown_list)
        self.click(show_all_projects_button)
        self._tab = ProjectAll(self._driver)

    def get_project_creation_form(self):
        self._tab = ProjectCreationForm(self._driver)

    def validate_name(self, name):
        try:
            self.find_element(page_name.replace('$(expected_name)', name))
            return True
        except NoSuchElementException:
            return False
