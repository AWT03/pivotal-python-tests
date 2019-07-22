from core.ui.pages.tab_page import TabPage
from pivotal_tracker.ui.pages.project_view.project_stories import ProjectStories
from pivotal_tracker.ui.pages.project_view.project_analytics import ProjectAnalytics
from pivotal_tracker.ui.pages.project_view.project_members import ProjectMembers
from pivotal_tracker.ui.pages.project_view.project_more import ProjectMore

project_stories_tab = '[data-aid="navTab-stories"]'
project_analytics_tab = '[data-aid="navTab-analytics"]'
project_members_tab = '[data-aid="navTab-members"]'
project_more_tab = '[data-aid="navTab-more"]'
background_div = '.scrim'


class ProjectMain(TabPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._tabs = {
            "Stories": lambda: self.get_stories_tab(),
            "Analytics": lambda: self.get_analytics_tab(),
            "Members": lambda: self.get_members_tab(),
            "More": lambda: self.get_more_tab()
        }
        self._tab = ProjectStories(self._driver)
        self.wait_for_hidden(background_div)

    def get_stories_tab(self):
        self.click(project_stories_tab)
        self._tab = ProjectStories(self._driver)

    def get_analytics_tab(self):
        self.click(project_analytics_tab)
        self._tab = ProjectAnalytics(self._driver)

    def get_members_tab(self):
        self.click(project_members_tab)
        self._tab = ProjectMembers(self._driver)

    def get_more_tab(self):
        self.click(project_more_tab)
        self._tab = ProjectMore(self._driver)
