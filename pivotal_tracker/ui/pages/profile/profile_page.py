from core.ui.pages.tab_page import TabPage
from pivotal_tracker.ui.pages.profile.profile_details import ProfileDetails
from pivotal_tracker.ui.pages.profile.accounts.profile_accounts import ProfileAccounts
from pivotal_tracker.ui.pages.profile.profile_notifications_settings import ProfileNotificationsSettings

go_details_button = 'div[class*="section"]  a[href*="profile"]'
go_accounts_button = 'div[class*="section"]  a[href*="accounts"]'
go_notifications_button = 'div[class*="section"]  a[href*="notification"]'


class ProfilePage(TabPage):
    def __init__(self, driver):
        super().__init__(driver)
        self._tabs = {
            "Details": lambda: self.get_details_tab(),
            "Accounts": lambda: self.get_accounts_tab(),
            "NotificationsSettings": lambda: self.get_notifications_settings_tab()
        }
        self._tab = ProfileDetails(self._driver)

    def get_details_tab(self):
        self.click(go_details_button)
        self._tab = ProfileDetails(self._driver)

    def get_accounts_tab(self):
        self.click(go_accounts_button)
        self._tab = ProfileAccounts(self._driver)

    def get_notifications_settings_tab(self):
        self.click(go_notifications_button)
        self._tab = ProfileNotificationsSettings(self._driver)
