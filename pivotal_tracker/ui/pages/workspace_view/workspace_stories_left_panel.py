from core.ui.pages.action_page import ActionPage
from core.ui.pages.tab_page import TabPage

project_counter = '//button[text()="$(expected_value)"]'


class WorkspaceStoriesLeftPanel(TabPage, ActionPage):
    def __init__(self, driver):
        super().__init__(driver)

    def validate_project_counter(self, value):
        return self.is_existing(project_counter.replace('$(expected_value)', value))

