from core.ui.pages.action_page import ActionPage

more_options = 'a[href*="/settings"]'
background_div = '.scrim'


class ProjectMainPage(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "More": lambda: self.more_settings()
        }
        self.update_actions(**actions)

    def more_settings(self):
        self.wait_until(background_div)
        self.click(more_options)
