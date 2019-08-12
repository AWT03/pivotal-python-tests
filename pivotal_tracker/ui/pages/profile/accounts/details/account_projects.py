from core.ui.pages.action_page import ActionPage

project_names = '.project_name'


class AccountProjects(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            'get_project_names': lambda: str([i.text for i in self.find_elements(project_names)])
        }
        self.update_actions(**actions)
