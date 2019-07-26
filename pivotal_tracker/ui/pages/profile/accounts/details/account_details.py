from core.ui.pages.tab_page import TabPage
from pivotal_tracker.ui.pages.profile.accounts.details.account_plans_billing import AccountPlansBilling
from pivotal_tracker.ui.pages.profile.accounts.details.account_settings import AccountSettings
from pivotal_tracker.ui.pages.profile.accounts.details.account_projects import AccountProjects
from pivotal_tracker.ui.pages.profile.accounts.details.account_members import AccountMembers

plans_billing_button = '//a[contains(@class, "button")][contains(text(), "Plans")]'
settings_button = '//a[contains(@class, "button")][contains(text(), "Settings")]'
projects_button = '//a[contains(@class, "button")][contains(text(), "Projects")]'
account_members_button = '//a[contains(@class, "button")][contains(text(), "Members")]'


class AccountDetails(TabPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._tabs = {
            "Plans&Billing": lambda: self.__get_plans_billing_tab(),
            "Settings": lambda: self.__get_settings_tab(),
            "Projects": lambda: self.__get_projects_tab(),
            "AccountMembers": lambda: self.__get_account_members()
        }
        self._tab = AccountPlansBilling(self._driver)

    def __get_plans_billing_tab(self):
        self.click(plans_billing_button)
        self._tab = AccountPlansBilling(self._driver)

    def __get_settings_tab(self):
        self.click(settings_button)
        self._tab = AccountSettings(self._driver)

    def __get_projects_tab(self):
        self.click(projects_button)
        self._tab = AccountProjects(self._driver)

    def __get_account_members(self):
        self.click(account_members_button)
        self._tab = AccountMembers(self._driver)
