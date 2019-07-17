from pivotal_tracker.ui.pages.user_header import UserHeader
from pivotal_tracker.ui.pages.dashboard.dashboard_page import DashboardPage
from pivotal_tracker.ui.pages.project_main import ProjectMain


class UserPage(UserHeader):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.tab_switch = {
            "Dashboard": lambda: self.get_dashboard_tab(),
            "ProjectMain": lambda: self.get_project_main_tab()
        }
        self.current_tab = DashboardPage(self.driver)

    def do_action(self, value):
        switch = self.current_tab.do_action(value)
        if switch in self.tab_switch:
            self.current_tab = self.tab_switch[switch]()
            return ''
        else:
            return switch

    def get_dashboard_tab(self):
        return DashboardPage(self.driver)

    def get_project_main_tab(self):
        return ProjectMain(self.driver)
