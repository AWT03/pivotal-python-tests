from core.ui.pages.base_page import BasePage
from pivotal_tracker.ui.pages.project_view.project_stories import ProjectStories
from pivotal_tracker.ui.pages.project_view.project_analytics import ProjectAnalytics
from pivotal_tracker.ui.pages.project_view.project_members import ProjectMembers
from pivotal_tracker.ui.pages.project_view.project_more import ProjectMore

project_stories_tab = '[data-aid="navTab-stories"]'
project_analytics_tab = '[data-aid="navTab-analytics"]'
project_members_tab = '[data-aid="navTab-members"]'
project_more_tab = '[data-aid="navTab-more"]'
background_div = '.scrim'


class ProjectMain(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.tab_switch = {
            "Stories": lambda: self.get_stories_tab(),
            "Analytics": lambda: self.get_analytics_tab(),
            "Members": lambda: self.get_members_tab(),
            "More": lambda: self.get_more_tab()
        }
        self.current_tab = ProjectStories(self._driver)

    def do_action(self, value):
        switch = self.current_tab.do_action(value)
        if switch in self.tab_switch:
            self.current_tab = self.tab_switch[switch]()
            return ''
        else:
            return switch

    def set_form(self, **values):
        self.current_tab.set_form(**values)

    def get_stories_tab(self):
        self.wait_until(background_div)
        self.click(project_stories_tab)
        return ProjectStories(self._driver)

    def get_analytics_tab(self):
        self.wait_until(background_div)
        self.click(project_analytics_tab)
        return ProjectAnalytics(self._driver)

    def get_members_tab(self):
        self.wait_until(background_div)
        self.click(project_members_tab)
        return ProjectMembers(self._driver)

    def get_more_tab(self):
        self.wait_until(background_div)
        self.click(project_more_tab)
        return ProjectMore(self._driver)
