from core.ui.pages.tab_page import TabPage
from pivotal_tracker.ui.pages.dashboard.dashboard_projects import DashboardProjects
from pivotal_tracker.ui.pages.dashboard.dashboard_workspaces import DashboardWorkspaces


class DashboardPage(TabPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._tabs = {
            "Projects": lambda: self.get_projects_tab(),
            "Workspaces": lambda: self.get_workspaces_tab()
        }
        self._tab = DashboardProjects(self._driver)

    def get_projects_tab(self):
        self._tab = DashboardProjects(self._driver)

    def get_workspaces_tab(self):
        self._tab = DashboardWorkspaces(self._driver)
