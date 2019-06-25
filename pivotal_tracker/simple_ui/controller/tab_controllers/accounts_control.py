from pivotal_tracker.simple_ui.controller.tab_controllers.tab_control import TabControl


class AccountsControl(TabControl):
    def __init__(self, view):
        super().__init__(view)
        self._tab = self._view.get_accounts_tab()
        self._connect_tab()

    def _update_api(self, summary=False):
        account_id = self._tab.get_id()
        if summary:
            self._api.build_end_point('account_summary')
        else:
            self._api.build_end_point('accounts', account_id)

    def _get_data(self):
        pass

    def _connect_tab(self):
        self._tab.get_get_button().clicked.connect(self._get_accounts)
        self._tab.get_get_summary_button().clicked.connect(self._get_accounts_summary)

    def _get_accounts(self):
        self._generic_get()

    def _get_accounts_summary(self):
        self._update_api(True)
        self._generic_get()
        self._show_response()
