from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.workspace_view.workspace_stories_sidebar import WorkspaceStoriesSideBar
from core.ui.pages.tab_page import TabPage
from core.ui.pages.element_search import ElementSearch
from pivotal_tracker.ui.pages.tabs.workspace_tabs import WorkspaceTabs

header_name = '//span[text()="$(expected_name)"]'
main_menu = '//span[text()="$(expected_name)"]'


class WorkspaceStories(ActionPage, TabPage, ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        self._search_elements = {

            "header_name": lambda value: self.validate_header_name(value),
        }
        self._tabs = {
            "SideBar": lambda: self.get_side_bar()
        }
        actions = {
            "Main menu": lambda value: self.open_main_menu(value)
        }
        self.update_actions(**actions)

    def get_side_bar(self):
        self._tab = WorkspaceStoriesSideBar(self._driver)

    def validate_header_name(self, name):
        return self.is_existing(header_name.replace('$(expected_name)', name))

    def open_main_menu(self, value):
        selector = main_menu.replace('$(expected_name)', value)
        self.click(selector)
        return WorkspaceTabs.MAIN_MENU
