from core.ui.pages.tab_page import TabPage
from pivotal_tracker.ui.pages.workspace_view.workspace_stories import WorkspaceStories
from pivotal_tracker.ui.pages.workspace_view.workspace_more import WorkspaceMore

workspace_more_tab = 'a[data-aid="navTab-more"]'
workspace_stories_tab = 'a[data-aid="navTab-stories"]'
workspace_settings = '#workspace_settings'
workspace_settings_item = '//a[text()="settings"]'


class WorkspaceMain(TabPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._tabs = {
            "Stories": lambda: self.get_stories_tab(),
            "More": lambda: self.get_more_tab()
        }
        self._tab = WorkspaceStories(self._driver)

    def get_stories_tab(self):
        self.click(workspace_stories_tab)
        self._tab = WorkspaceStories(self._driver)

    def get_more_tab(self):
        self.click(workspace_more_tab)
        self._tab = WorkspaceMore(self._driver)

