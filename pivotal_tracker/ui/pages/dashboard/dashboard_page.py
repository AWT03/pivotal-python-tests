from core.ui.pages.tab_page import TabPage
from pivotal_tracker.ui.pages.dashboard.dashboard_projects import DashboardProjects
from pivotal_tracker.ui.pages.dashboard.dashboard_workspaces import DashboardWorkspaces
from pivotal_tracker.ui.pages.pop_ups.workspace_creation_form import WorkspaceCreationForm
from pivotal_tracker.ui.pages.workspace_view.workspace_main import WorkspaceMain

go_workspace_tab = '//span[text()="Workspaces"]'


class DashboardPage(TabPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._tabs = {
            "Projects": lambda: self.get_projects_tab(),
            "Workspaces": lambda: self.get_workspaces_tab(),
            "WorkspaceCreation": lambda: self.get_workspace_creation_form(),
            "WorkspaceMain": lambda: self.get_workspace_main_tab()
        }
        self._tab = DashboardProjects(self._driver)

    def get_projects_tab(self):
        self._tab = DashboardProjects(self._driver)

    def get_workspaces_tab(self):
        self.click(go_workspace_tab)
        self._tab = DashboardWorkspaces(self._driver)

    def get_workspace_creation_form(self):
        self._tab = WorkspaceCreationForm(self._driver)

    def get_workspace_main_tab(self):
        self._tab = WorkspaceMain(self._driver)