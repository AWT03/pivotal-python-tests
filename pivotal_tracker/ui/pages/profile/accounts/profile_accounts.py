from core.ui.pages.tab_page import TabPage
from pivotal_tracker.ui.pages.profile.accounts.accounts_list import AccountsList
from pivotal_tracker.ui.pages.profile.accounts.details.account_details import AccountDetails

create_account_button = '.create_account_button'
new_account_name_field = '.tc-form__input'
action_create = 'button[type="submit"]'


class ProfileAccounts(TabPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._tabs = {
            "AccountsList": lambda: self.get_accounts_list_tab(),
            "AccountDetails": lambda: self.get_account_details_tab()
        }
        self._tab = AccountsList(self._driver)

    def get_accounts_list_tab(self):
        self._tab = AccountsList(self._driver)

    def get_account_details_tab(self):
        self._tab = AccountDetails(self._driver)
