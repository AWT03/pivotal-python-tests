from core.ui.pages.action_page import ActionPage
from core.ui.pages.form_page import FormPage
from selenium.common.exceptions import NoSuchElementException
from core.ui.pages.element_search import ElementSearch
from pivotal_tracker.ui.pages.tabs.workspace_tabs import WorkspaceTabs

workspace_title_field = 'input[class="settings_field"][value="$(name)"]'
header_name_more = '//div[text()="$(expected_name)"]'
delete_selector = '//a[text()="Delete"]'
delete_submit = '#confirm_delete'
go_dashboard_button = '.headerLogo__image'
edit_saved_changes_sms = '//div[@id="save_success_bar"]//following-sibling::div[1][text()="$(message)"]'
save_button = 'input[name="commit"][value="Save"]'
workspace_title_field_edit = 'input[class="settings_field"]'

field_map = {
    "workspace_name": workspace_title_field
}

sms_map = {
    "changes_saved": "Changes saved."
}


class WorkspaceMore(ActionPage, ElementSearch, FormPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._search_elements = {
            "header_name_more": lambda value: self.validate_header_name_more(value)
        }
        actions = {
            "Header Logo": lambda: self.click_header_logo(),
            "Delete": lambda: self.delete_workspace(),
            "Save": lambda: self.save_workspace()
        }
        fields = {
            "workspace_name": lambda value: self.set_value(workspace_title_field_edit, value)
        }
        self.update_actions(**actions)
        self.update_form_fields(**fields)

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

    def save_workspace(self):
        self.click(save_button)

    def verify_save_message(self, message):
        element = self.find_element(edit_saved_changes_sms.replace("$(message)", sms_map[message]))
        is_visible = False
        if element:
            is_visible = True if element.is_displayed() else False
        return is_visible
