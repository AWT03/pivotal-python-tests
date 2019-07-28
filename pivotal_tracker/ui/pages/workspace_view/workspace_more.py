from core.ui.pages.action_page import ActionPage
from selenium.common.exceptions import NoSuchElementException
from core.ui.pages.element_search import ElementSearch
from pivotal_tracker.ui.pages.tabs.workspace_tabs import WorkspaceTabs
from pivotal_tracker.ui.pages.dashboard.dashboard_page import DashboardPage

workspace_title_field = 'input[class="settings_field"][value="$(name)"]'
header_name_more = '//div[text()="$(expected_name)"]'
delete_selector = '//a[text()="Delete"]'
delete_submit = '#confirm_delete'
go_dashboard_button = '.headerLogo__image'

field_map = {
    "workspace_name": workspace_title_field
}


class WorkspaceMore(ActionPage, ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        self._search_elements = {
            "header_name_more": lambda value: self.validate_header_name_more(value)
        }
        actions = {
            "Header Logo": lambda: self.click_header_logo(),
            "Delete": lambda: self.delete_workspace()
        }
        self.update_actions(**actions)

    def match_fields(self, **values):
        for tag in values:
            try:
                field_ref = field_map[tag]
                self.find_element(field_ref.replace('$(name)', values[tag]))
            except NoSuchElementException:
                return False
        return True

    def validate_header_name_more(self, name):
        return self.is_existing(header_name_more.replace('$(expected_name)', name))

    def validate_option_displayed(self, option):
        return self.is_existing(delete_selector.replace('$(option)', option))

    def click_header_logo(self):
        self.click(go_dashboard_button)
        return WorkspaceTabs.DASHBOARD

    def delete_workspace(self):
        self.click(delete_selector)
        self.click(delete_submit)
        return WorkspaceTabs.DASHBOARD_ONLY
