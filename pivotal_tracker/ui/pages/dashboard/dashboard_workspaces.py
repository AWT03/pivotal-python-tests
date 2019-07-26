from core.ui.pages.action_page import ActionPage
from core.ui.pages.element_search import ElementSearch
from pivotal_tracker.ui.pages.tabs.workspace_tabs import WorkspaceTabs

workspace_title_field = '//div[@class="WorkspaceTile"]/div/a[@class="WorkspaceTile__name"][text()="$(workspace_name)"]'
create_workspace_button = '#create-workspace-button'
workspace_list = '//a[@class="WorkspaceTile__name"][text()="$(workspace_name)"]'
workspace_sms_projects = '//div[@class="WorkspaceTile"]/div/a[@class="WorkspaceTile__name"][text()="$(workspace_name)"]' \
        '//ancestor::div[1]//following-sibling::div[text()="$(sms_projects)"]'
workspace_settings = '//div[@class="WorkspaceTile"]/div/a[@class="WorkspaceTile__name"][text()="$(workspace_name)"]' \
        '//following-sibling::span[@data-balloon="Workspace settings"]/a'

workspace_sms = {
    "workspace_without_projects": "You haven't added any projects to this workspace."
}


class DashboardWorkspaces(ActionPage, ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "Create workspace": lambda: self.open_create_workspace_form(),
            "Workspace settings": lambda value: self.open_workspace_more_settings(value),
            "Workspace name": lambda value: self.open_workspace_created(value)
        }
        search_elements = {
            "workspaces_list": lambda value: self.workspace_exists_in_list(value)
        }
        self.update_actions(**actions)
        self.update_search_fields(**search_elements)

    def open_create_workspace_form(self):
        self.click(create_workspace_button)
        return WorkspaceTabs.WORKSPACE_CREATION

    def workspace_exists_in_list(self, name):
        return self.is_existing(workspace_list.replace('$(workspace_name)', name))

    def validate_sms_in_workspace(self, sms, tag):
        selector = workspace_sms_projects.replace('$(workspace_name)', tag)
        selector = selector.replace('$(sms_projects)', workspace_sms.get(sms))
        return self.is_existing(selector)

    def open_workspace_more_settings(self, value):
        selector = workspace_settings.replace('$(workspace_name)', value)
        self.click(selector)
        return WorkspaceTabs.WORKSPACE_MORE

    def open_workspace_created(self, value):
        selector = workspace_title_field.replace('$(workspace_name)', value)
        self.click(selector)
        return WorkspaceTabs.WORKSPACE_STORY
