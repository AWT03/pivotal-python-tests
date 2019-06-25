from pivotal_tracker.simple_ui.controller.tab_controllers.tab_control import TabControl


class WorkspacesControl(TabControl):
    def __init__(self, view):
        super().__init__(view)
        self._tab = self._view.get_workspaces_tab()
        self._connect_tab()

    def _update_api(self):
        workspace_id = self._tab.get_id()
        self._api.build_end_point('workspaces', workspace_id)

    def _get_data(self):
        return self._tab.get_put_post_data()

    def _connect_tab(self):
        self._tab.get_get_button().clicked.connect(self._get_workspaces)
        self._tab.get_put_button().clicked.connect(self._put_workspace)
        self._tab.get_post_button().clicked.connect(self._post_workspace)
        self._tab.get_delete_button().clicked.connect(self._delete_workspace)

    def _get_workspaces(self):
        self._generic_get()

    def _put_workspace(self):
        self._generic_put()

    def _post_workspace(self):
        self._generic_post()

    def _delete_workspace(self):
        self._generic_delete()
