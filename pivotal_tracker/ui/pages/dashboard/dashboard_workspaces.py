from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.tabs.dashboard_tabs import DashboardTabs as DT


class DashboardWorkspaces(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
