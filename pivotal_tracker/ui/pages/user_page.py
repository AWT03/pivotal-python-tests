from core.ui.pages.base_page import BasePage
from pivotal_tracker.ui.pages.dashboard.dashboard_page import DashboardPage
from pivotal_tracker.ui.pages.project_view.project_main import ProjectMain
from pivotal_tracker.ui.pages.project_view.projects_all import ProjectAll
from pivotal_tracker.ui.pages.pop_ups.project_creation_form import ProjectCreationForm
from selenium.common.exceptions import NoSuchElementException

go_dashboard_button = '.headerLogo__image'
page_name = '//span[text()="$(expected_name)"]'
projects_dropdown_list = '.tc_projects_dropdown_link.tc_context_name'
show_all_projects_button = '//span[text()="Show All Projects"]'


class UserPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.tab_switch = {
            "Dashboard": lambda: self.get_dashboard_tab(),
            "ProjectMain": lambda: self.get_project_main_tab(),
            "AllProjects": lambda: self.get_all_projects(),
            "ProjectCreation": lambda: self.get_project_creation_form()
        }
        self.current_tab = DashboardPage(self._driver)

    def do_action(self, value):
        switch = self.current_tab.do_action(value)
        if switch in self.tab_switch:
            self.current_tab = self.tab_switch[switch]()
            return ''
        else:
            return switch

    def set_form(self, **values):
        self.current_tab.set_form(**values)

    def get_dashboard_tab(self):
        return DashboardPage(self._driver)

    def get_project_main_tab(self):
        return ProjectMain(self._driver)

    def get_all_projects(self):
        return ProjectAll(self._driver)

    def get_project_creation_form(self):
        return ProjectCreationForm(self._driver)

    def go_to_all_projects(self):
        self.click(projects_dropdown_list)
        self.click(show_all_projects_button)
        self.current_tab = self.tab_switch['AllProjects']()

    def go_to_dashboard(self):
        self.click(go_dashboard_button)
        self.current_tab = self.tab_switch['Dashboard']()
        self.current_tab.current_tab = self.current_tab.tab_switch["Projects"]()

    def validate_name(self, name):
        try:
            self.find_element(page_name.replace('$(expected_name)', name))
            return True
        except NoSuchElementException:
            return False
