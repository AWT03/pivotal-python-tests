from core.ui.pages.element_search import ElementSearch
from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.tabs.workspace_tabs import WorkspaceTabs


workspace_list = '//div[@class="workspaces column"]/a[text()="$(workspace_name)"]'
project_count_sms = '//div[@class="workspaces column"]/a[text()="$(workspace_name)"]//ancestor::div[1]//following-sibling::div[@class="project_colors column"]/span[text()="$(sms_projects)"]'
project_count = '//div[@class="workspaces column"]/a[text()="$(workspace_name)"]//ancestor::div[1]//following-sibling::div[2]'
workspace_settings = '//div[@class="workspaces column"]/a[text()="$(workspace_name)"]//ancestor::div[1]//following-sibling::div[3]/div/a'
workspace_title_field = '//div[@class="workspaces column"]/a[text()="$(workspace_name)"]'


class WorkspacesShowAll(ElementSearch, ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        search_elements = {
            "workspaces_list": lambda value: self.workspace_exists_in_list(value)
        }
        actions = {
            "Settings": lambda value: self.open_settings_workspace(value),
            "Workspace name": lambda value: self.open_workspace_created(value)
        }
        self.update_actions(**actions)
        self.update_search_fields(**search_elements)

    def workspace_exists_in_list(self, name):
        return self.is_existing(workspace_list.replace('$(workspace_name)', name))

    def get_value_projects_counter_sms(self, value, name):
        selector = project_count_sms.replace('$(sms_projects)', value)
        selector = selector.replace('$(workspace_name)', name)
        return self.get_value(selector)


    def get_value_projects_counter(self, name):
        selector = project_count.replace('$(workspace_name)', name)
        return self.get_value(selector)

    def open_settings_workspace(self, value):
        selector = workspace_settings.replace('$(workspace_name)', value)
        self.click(selector)
        return WorkspaceTabs.WORKSPACE_MORE

    def open_workspace_created(self, value):
        selector = workspace_title_field.replace('$(workspace_name)', value)
        self.click(selector)
        return WorkspaceTabs.STORIES
