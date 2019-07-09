from core.ui.pages.base_page import BasePage


class ActionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._actions = {}

    def update_actions(self, **fields):
        for tag in fields:
            self._actions[tag] = fields[tag]

    def do_action(self, action_id):
        if action_id in self._actions:
            return self._actions[action_id]()
