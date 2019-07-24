from core.ui.pages.form_page import FormPage
from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.tabs.user_main_tabs import UserMainTabs

workspace_name_field = '.tc-form__input'
create_button = 'button[data-aid="FormModal__submit"]'
background_div = '.scrim'


class WorkspaceCreationForm(FormPage, ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        fields = {
            "workspace_name": lambda value: self.set_value(workspace_name_field, value)
        }
        actions = {
            "Create": lambda: self.create_workspace()
        }
        self.update_actions(**actions)
        self.update_form_fields(**fields)

    def create_workspace(self):
        self.click(create_button)
        self.wait_for_hidden(background_div)
        return UserMainTabs.WORKSPACE_MAIN
