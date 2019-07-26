from core.ui.pages.action_page import ActionPage
from core.ui.pages.element_search import ElementSearch
from pivotal_tracker.ui.pages.tabs.workspace_tabs import WorkspaceTabs

main_menu = '//span[text()="$(expected_name)"]'
project_counter = '//button[text()="$(expected_value)"]'
workspace_settings = '#workspace_settings'
workspace_settings_item = '//a[text()="settings"]'


class WorkspaceStories(ActionPage, ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        self._search_elements = {
            "project_counter": lambda value: self.validate_project_counter(value),
        }
        actions = {
            "Main menu": lambda value: self.open_main_menu(value),
            "Open Workspace Settings": lambda: self.get_settings_tab()
        }
        self.update_actions(**actions)

    def open_main_menu(self, value):
        selector = main_menu.replace('$(expected_name)', value)
        self.click(selector)
        return WorkspaceTabs.MAIN_MENU

    def validate_project_counter(self, value):
        return self.is_existing(project_counter.replace('$(expected_value)', value))

    def get_settings_tab(self):
        window_before = self._driver.window_handles[0]
        self.click(workspace_settings)
        self.click(workspace_settings_item)
        window_after = self._driver.window_handles[1]
        self._driver.switch_to_window(window_after)
        return 'More'
