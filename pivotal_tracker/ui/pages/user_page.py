from core.ui.pages.tab_page import TabPage
from core.ui.pages.element_search import ElementSearch
from pivotal_tracker.ui.pages.dashboard.dashboard_page import DashboardPage
from pivotal_tracker.ui.pages.project_view.project_main import ProjectMain
from pivotal_tracker.ui.pages.project_view.projects_all import ProjectAll
from pivotal_tracker.ui.pages.profile.profile_page import ProfilePage
from pivotal_tracker.ui.pages.pop_ups.project_creation_form import ProjectCreationForm
from pivotal_tracker.ui.pages.pop_ups.workspace_creation_form import WorkspaceCreationForm
from pivotal_tracker.ui.pages.workspace_view.workspace_main import WorkspaceMain
from pivotal_tracker.ui.pages.workspace_view.workspace_more import WorkspaceMore
from pivotal_tracker.ui.pages.pop_ups.main_menu import MainMenu
from pivotal_tracker.ui.pages.workspace_view.workspaces_show_all import WorkspacesShowAll
from pivotal_tracker.ui.pages.workspace_view.workspace_stories import WorkspaceStories

go_dashboard_button = '.headerLogo__image'
projects_dropdown_list = '.tc_projects_dropdown_link.tc_context_name'
header_name = '//span[text()="$(expected_name)"]'
header_name_more = '//div[text()="$(expected_name)"]'
header_privacy = '//span[text()="($(privacy))"]'
show_all_projects_button = '//span[text()="Show All Projects"]'
show_all_workspaces_button = '//span[text()="Show All Projects"]'
user_options_dropdown = 'button[aria-label="Profile Dropdown"]'
profile_details_button = 'a[href*="/profile"][class*="Dropdown"]'


class UserPage(TabPage, ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        self._search_elements = {
            "header_name": lambda value: self.validate_header_name(value),
            "header_name_more": lambda value: self.validate_header_name_more(value),
            "header_privacy": lambda value: self.validate_header_privacy(value)
        }
        self._tabs = {
            "Dashboard": lambda: self.get_dashboard_tab(),
            "ProjectMain": lambda: self.get_project_main_tab(),
            "AllProjects": lambda: self.get_all_projects(),
            "ProjectCreation": lambda: self.get_project_creation_form(),
            "Profile": lambda: self.get_profile_tab(),
            "WorkspaceCreation": lambda: self.get_workspace_creation_form(),
            "WorkspaceMain": lambda: self.get_workspace_main_tab(),
            "WorkspaceStory": lambda: self.get_workspace_story_tab(),
            "AllWorkspaces": lambda: self.get_show_all_workspaces(),
            "MainMenu": lambda: self.get_main_menu()
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

    def get_profile_tab(self):
        self.click(user_options_dropdown)
        self.click(profile_details_button)
        self._tab = ProfilePage(self._driver)

    def validate_header_name(self, name):
        return self.is_existing(header_name.replace('$(expected_name)', name))

    def validate_header_privacy(self, privacy):
        return self.is_existing(header_privacy.replace('$(privacy)', privacy))

    def get_workspace_creation_form(self):
        self._tab = WorkspaceCreationForm(self._driver)

    def get_workspace_main_tab(self):
        self._tab = WorkspaceMain(self._driver)

    def get_workspace_more_tab(self):
        self._tab = WorkspaceMore(self._driver)

    def get_workspace_story_tab(self):
        self._tab = WorkspaceStories(self._driver)

    def validate_header_name_more(self, name):
        return self.is_existing(header_name_more.replace('$(expected_name)', name))

    def get_all_workspaces(self):
        self.click(projects_dropdown_list)
        self.click(show_all_workspaces_button)
        self._tab = WorkspacesShowAll(self._driver)

    def get_story(self):
        self._tab = WorkspaceStories(self._driver)

    def get_main_menu(self):
        self.click(projects_dropdown_list)
        self._tab = MainMenu(self._driver)

    def get_show_all_workspaces(self):
        self.click(projects_dropdown_list)
        self.click(show_all_workspaces_button)
        self._tab = WorkspacesShowAll(self._driver)

    def get_search_keys(self):
        return list(self._search_elements.keys())
