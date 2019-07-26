from core.ui.pages.action_page import ActionPage
from core.ui.pages.element_search import ElementSearch
from pivotal_tracker.ui.pages.tabs.workspace_tabs import WorkspaceTabs

workspace_title = '//span[@class="raw_workspace_name"][text()="$(workspace_title)"]'
all_workspaces_list = 'a[href*="/workspaces/"][class="tc_projects_menu_item_link"]'
ref_all_workspaces = 'a[href*="/projects"][class="tc_projects_menu_show_all"]'


class MainMenu(ActionPage, ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        search_elements = {
            "workspaces_list": lambda value: self.workspace_exists_in_list(value)
        }
        actions = {
            "Show All Workspaces": lambda: self.open_show_all_workspaces()
        }
        self.update_actions(**actions)
        self.update_search_fields(**search_elements)

    def workspace_exists_in_list(self, name):
        length = len(self.find_elements(all_workspaces_list))
        if length <=11:
            return self.is_existing(workspace_title.replace('$(workspace_title)', name))
        return False

    def open_show_all_workspaces(self):
        self.click(ref_all_workspaces)
        return WorkspaceTabs.SHOW_ALL_WORKSPACES
