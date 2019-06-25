from PyQt5.QtWidgets import QMainWindow
from pivotal_tracker.simple_ui.view.main_widget import MainWidget


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__main_widget = MainWidget()

    def init_ui(self):
        self.setCentralWidget(self.__main_widget)
        self.showMaximized()

    def post_message(self, value):
        self.__main_widget.set_console_message(value)

    def get_projects_tab(self):
        return self.__main_widget.get_project_tab()

    def get_stories_tab(self):
        return self.__main_widget.get_stories_tab()

    def get_tasks_tab(self):
        return self.__main_widget.get_tasks_tab()

    def get_comments_tab(self):
        return self.__main_widget.get_comments_tab()

    def get_workspaces_tab(self):
        return self.__main_widget.get_workspaces_tab()

    def get_accounts_tab(self):
        return self.__main_widget.get_accounts_tab()

    def set_request_status(self, value):
        self.__main_widget.set_request_status(value)
