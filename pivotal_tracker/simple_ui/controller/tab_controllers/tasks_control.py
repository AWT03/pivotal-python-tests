from pivotal_tracker.simple_ui.controller.tab_controllers.tab_control import TabControl


class TasksControl(TabControl):
    def __init__(self, view):
        super().__init__(view)
        self._tab = self._view.get_tasks_tab()
        self._connect_tab()

    def _update_api(self):
        project_id = self._tab.get_project_id()
        story_id = self._tab.get_story_id()
        task_id = self._tab.get_id()
        self._api.build_end_point('tasks', project_id, story_id, task_id)

    def _get_data(self):
        return self._tab.get_put_post_data()

    def _connect_tab(self):
        self._tab.get_get_button().clicked.connect(self._get_tasks)
        self._tab.get_put_button().clicked.connect(self._put_task)
        self._tab.get_post_button().clicked.connect(self._post_task)
        self._tab.get_delete_button().clicked.connect(self._delete_task)

    def _get_tasks(self):
        self._generic_get()

    def _put_task(self):
        self._generic_put()

    def _post_task(self):
        self._generic_post()

    def _delete_task(self):
        self._generic_delete()
