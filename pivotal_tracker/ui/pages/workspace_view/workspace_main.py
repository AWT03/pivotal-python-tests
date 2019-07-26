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
            "More": lambda: self.get_more_tab(),
            "WorkspaceSettings": lambda: self.get_settings_tab()
        }
        self._tab = WorkspaceStories(self._driver)

    def get_stories_tab(self):
        self.click(workspace_stories_tab)
        self._tab = WorkspaceStories(self._driver)

    def get_more_tab(self):
        self.click(workspace_more_tab)
        self._tab = WorkspaceMore(self._driver)

    def get_settings_tab(self):
        window_before = self._driver.window_handles[0]
        self.click(workspace_settings)
        print(window_before)
        self.click(workspace_settings_item)
        window_after = self._driver.window_handles[1]
        self._driver.switch_to_window(window_after)
        self._tab = WorkspaceMore(self._driver)
