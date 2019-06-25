from pivotal_tracker.simple_ui.controller.tab_controllers.projects_control import ProjectsControl
from pivotal_tracker.simple_ui.controller.tab_controllers.stories_control import StoriesControl
from pivotal_tracker.simple_ui.controller.tab_controllers.tasks_control import TasksControl
from pivotal_tracker.simple_ui.controller.tab_controllers.comments_control import CommentsControl
from pivotal_tracker.simple_ui.controller.tab_controllers.workspaces_control import WorkspacesControl
from pivotal_tracker.simple_ui.controller.tab_controllers.accounts_control import AccountsControl


class Controller:
    def __init__(self, view):
        self.__view = view
        self.__view.init_ui()
        self.__projects_control = ProjectsControl(view)
        self.__stories_control = StoriesControl(view)
        self.__tasks_control = TasksControl(view)
        self.__comment_control = CommentsControl(view)
        self.__workspaces_control = WorkspacesControl(view)
        self.__accounts_control = AccountsControl(view)
