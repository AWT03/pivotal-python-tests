from core.ui.pages.tab_page import TabPage
from pivotal_tracker.ui.pages.stories.stories_backlog import StoriesBacklog


class StoriesPage(TabPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._tabs = {
            "story_backlog": lambda: self.get_stories_backlog_tab(),
        }
        self._tab = StoriesBacklog(self._driver)

    def get_stories_backlog_tab(self):
        self._tab = StoriesBacklog(self._driver)
