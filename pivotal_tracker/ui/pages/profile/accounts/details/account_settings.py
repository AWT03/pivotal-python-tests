from core.ui.pages.action_page import ActionPage

delete_account_button = 'a[data-method="delete"]'
header_my_accounts = '//h2[contains(text(), "Own")]'


class AccountSettings(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "delete this account": lambda: self.__delete_this_account()
        }
        self.update_actions(**actions)

    def __delete_this_account(self):
        self.click(delete_account_button)
        self.get_driver().switch_to_alert().accept()
        self.wait_for_visible(header_my_accounts)
        return 'AccountsList'
