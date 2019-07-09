from core.ui.pages.action_page import ActionPage

more_options = 'a[href*="/settings"]'


class ProjectMainPage(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "More": lambda: self.click_more_button()
        }
        self.update_actions(**actions)

    def click_more_button(self):
        self.click(more_options, '.scrim')
