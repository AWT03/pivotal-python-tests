from core.ui.pages.form_page import FormPage
from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.dashboard_page import DashboardPage

username_field = 'input[id="credentials_username"]'
password_field = 'input[id="credentials_password"]'
signin_button = 'input[class="app_signin_action_button"]'


class LoginPage(FormPage, ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "sign_in_as": lambda value: self.set_username(value),
            "password": lambda value: self.set_password(value)
        }
        actions = {
            "Sign In": lambda: self.sign_in()
        }
        self.update_form_fields(**fields)
        self.update_actions(**actions)

    def set_username(self, value):
        self.set_value(username_field, value)
        self.click(signin_button)

    def set_password(self, value):
        self.set_value(password_field, value)

    def sign_in(self):
        self.click(signin_button)
        return DashboardPage(self._driver)
