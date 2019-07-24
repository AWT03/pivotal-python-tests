from core.ui.pages.action_page import ActionPage

delete_account_button = 'a[data-method="delete"]'


class AccountSettings(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "delete this account": lambda: self.__delete_this_account()
        }
        self.update_actions(**actions)

    def __delete_this_account(self):
        self.click(delete_account_button)
        driver = self.get_driver()
        driver.switch_to_alert().accept()
        return 'AccountsList'
