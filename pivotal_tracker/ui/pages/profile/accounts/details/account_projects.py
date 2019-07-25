from core.ui.pages.action_page import ActionPage


class AccountProjects(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
        }
        self.update_actions(**actions)
