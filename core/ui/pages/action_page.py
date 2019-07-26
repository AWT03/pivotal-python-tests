from core.ui.pages.element import Element


class ActionPage(Element):
    def __init__(self, driver):
        super().__init__(driver)
        self._actions = {}

    def update_actions(self, **fields):
        for tag in fields:
            self._actions[tag] = fields[tag]

    def do_action(self, action_id, *params):
        if action_id in self._actions:
            return self._actions[action_id](*params)
