from core.ui.pages.action_page import ActionPage
from core.ui.pages.element_search import ElementSearch

delete_account_button = 'a[data-method="delete"]'
header_my_accounts = '//h2[contains(text(), "Own")]'
account_name_field = 'input[name="account[name]"][value="$(account_name)"]'
account_id_field = '//h4[text()="ID"]/following-sibling::div'


class AccountSettings(ActionPage, ElementSearch):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "delete this account": lambda: self.__delete_this_account(),
            "get_account_id": lambda: self.find_element(account_id_field).text
        }
        search_elements = {
            "Account Name": lambda value: self.__verify_account_name(value)
        }
        self.update_actions(**actions)
        self.update_search_fields(**search_elements)

    def __delete_this_account(self):
        self.click(delete_account_button)
        self.get_driver().switch_to_alert().accept()
        self.wait_for_visible(header_my_accounts)
        return 'AccountsList'

    def __verify_account_name(self, value):
        return self.is_existing(account_name_field.replace('$(account_name)', value))
