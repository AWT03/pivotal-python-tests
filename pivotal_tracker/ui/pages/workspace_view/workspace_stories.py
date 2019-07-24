from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.workspace_view.workspace_stories_left_panel import WorkspaceStoriesLeftPanel
from core.ui.pages.tab_page import TabPage


class WorkspaceStories(ActionPage, TabPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._tabs = {
            "LeftPanel": lambda: self.get_left_panel()
        }

    def get_left_panel(self):
        self._tab = WorkspaceStoriesLeftPanel(self._driver)
