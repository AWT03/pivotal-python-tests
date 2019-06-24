from pivotal_tracker.simple_ui.controller.tab_controllers.tab_control import TabControl


class ProjectsControl(TabControl):
    def __init__(self, view):
        super().__init__(view)
        self._tab = self._view.get_projects_tab()
        self._connect_tab()

    def _update_api(self):
        project_id = self._tab.get_id()
        self._api.build_end_point('projects', project_id)

    def _get_data(self):
        return self._tab.get_put_post_data()

    def _connect_tab(self):
        self._tab.get_get_button().clicked.connect(self._get_projects)
        self._tab.get_put_button().clicked.connect(self._put_project)
        self._tab.get_post_button().clicked.connect(self._post_project)
        self._tab.get_delete_button().clicked.connect(self._delete_project)

    def _get_projects(self):
        self._generic_get()

    def _put_project(self):
        self._generic_put()

    def _post_project(self):
        self._generic_post()

    def _delete_project(self):
        self._generic_delete()
