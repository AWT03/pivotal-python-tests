from core.ui.pages.element_search import ElementSearch
from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.tabs.user_main_tabs import UserMainTabs

project_list = '//a[@class="project_name"][text()="$(project_name)"]'
account_list = '//div[contains(@class,"account")]/a[text()="$(account)"]'
create_project_button = '//a[text()="Create Project"]'


class ProjectAll(ElementSearch, ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        search_elements = {
            "projects_list": lambda value: self.project_exists_in_list(value),
            "account_list": lambda value: self.account_exist_in_list(value)
        }
        actions = {
            "Create Project": lambda: self.open_create_project_form()
        }
        self.update_actions(**actions)
        self.update_search_fields(**search_elements)

    def open_create_project_form(self):
        self.click(create_project_button)
        return UserMainTabs.PROJECT_CREATION

    def project_exists_in_list(self, name):
        return self.is_existing(project_list.replace('$(project_name)', name))

    def account_exist_in_list(self, account_name):
        return self.is_existing(account_list.replace('$(account)', account_name))
