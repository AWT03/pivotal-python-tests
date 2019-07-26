from core.ui.pages.action_page import ActionPage

create_account_button = '.create_account_button'
new_account_name_field = '.tc-form__input'
action_create = 'button[type="submit"]'
manage_specific_account_button = '//div[@class="header"]/h3//div[text()="$(account_name)"]/' \
                                 'ancestor::div[@class="header"]/a[contains(@href, "/accounts")]'


class AccountsList(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "Create Account": lambda value: self.__create_account(value),
            "Manage Account": lambda value: self.__manage_account(value)
        }
        self.update_actions(**actions)

    def __create_account(self, name):
        self.click(create_account_button)
        self.set_value(new_account_name_field, name)
        self.click(action_create)
        self.wait_for_hidden('.scrim')
        return 'AccountDetails'

    def __manage_account(self, name):
        self.click(manage_specific_account_button.replace('$(account_name)', name))
        return 'AccountDetails'
