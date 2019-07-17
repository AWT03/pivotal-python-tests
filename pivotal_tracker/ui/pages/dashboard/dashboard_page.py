from pivotal_tracker.ui.pages.dashboard.dashboard_projects import DashboardProjects
from pivotal_tracker.ui.pages.dashboard.dashboard_workspaces import DashboardWorkspaces


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.tab_switch = {
            "Projects": lambda: self.get_projects_tab(),
            "Workspaces": lambda: self.get_workspaces_tab()
        }
        self.current_tab = DashboardProjects(self.driver)

    def do_action(self, value):
        switch = self.current_tab.do_action(value)
        if switch in self.tab_switch:
            self.current_tab = self.tab_switch[switch]()
            return ''
        else:
            return switch

    def get_projects_tab(self):
        return DashboardProjects(self.driver)

    def get_workspaces_tab(self):
        return DashboardWorkspaces(self.driver)
