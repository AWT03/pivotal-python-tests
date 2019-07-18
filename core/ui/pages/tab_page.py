from core.ui.pages.base_page import BasePage


class TabPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._tabs = {}
        self._tab = None

    def update_tabs(self, **tabs):
        for tag in tabs:
            self._tabs[tag] = tabs[tag]

    def go_to(self, tab):
        self._tabs[tab]()

    def do_action(self, value):
        switch = self._tab.do_action(value)
        if switch in self._tabs:
            self.go_to(switch)
            return ''
        return switch

    def get_tab(self):
        return self._tab
