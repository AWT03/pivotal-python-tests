from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTabWidget, QTextEdit, QLabel
from PyQt5.QtCore import Qt
from pivotal_tracker.simple_ui.view.chuchusmote_splitter import ChuchusmoteSplitter
from pivotal_tracker.simple_ui.view.tabs.projects_widget import ProjectsWidget
from pivotal_tracker.simple_ui.view.tabs.stories_widget import StoriesWidget
from pivotal_tracker.simple_ui.view.tabs.tasks_widget import TasksWidget
from pivotal_tracker.simple_ui.view.tabs.comments_widget import CommentsWidget
from pivotal_tracker.simple_ui.view.tabs.workspaces_widget import WorkspacesWidget
from pivotal_tracker.simple_ui.view.tabs.accounts_widget import AccountsWidget


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__console = QTextEdit()
        self.__console.setStyleSheet("QTextEdit{background-color: #222222; "
                                     "color: white; font-size: 16px}")
        self.__console.setReadOnly(True)
        self.__console_title = QLabel('CONSOLE')
        self.__console_title.setAlignment(Qt.AlignCenter)
        self.__console_title.setStyleSheet("QLabel{font-size: 18px; bold: True;}")
        self.__status = QLabel('Status: -')
        self.__status.setAlignment(Qt.AlignRight)
        self.__status.setStyleSheet("QLabel{font-size: 16px; bold: True;}")
        self.__side_panel = QTabWidget()
        self.__projects_tab = ProjectsWidget()
        self.__stories_tab = StoriesWidget()
        self.__tasks_tab = TasksWidget()
        self.__comments_tab = CommentsWidget()
        self.__workspaces_tab = WorkspacesWidget()
        self.__accounts_tab = AccountsWidget()
        self.__side_panel.addTab(self.__projects_tab, 'Projects')
        self.__side_panel.addTab(self.__stories_tab, 'Stories')
        self.__side_panel.addTab(self.__tasks_tab, 'Tasks')
        self.__side_panel.addTab(self.__comments_tab, 'Comments')
        self.__side_panel.addTab(self.__workspaces_tab, 'Workspaces')
        self.__side_panel.addTab(self.__accounts_tab, 'Accounts')
        self.__split_main_window()

    def __split_main_window(self):
        h_widgets = [
            (self.__console_title, 10),
            (self.__status, 10),
            (self.__console, 1000)
        ]
        horizontal = ChuchusmoteSplitter(h_widgets).vertical_split()
        v_widgets = [
            (self.__side_panel, 350),
            (horizontal, 650),
        ]
        vertical = ChuchusmoteSplitter(v_widgets).horizontal_split()
        box = QHBoxLayout(self)
        box.addWidget(vertical)
        self.setLayout(box)

    def set_console_message(self, value):
        self.__console.setText(value)

    def get_project_tab(self):
        return self.__projects_tab

    def get_stories_tab(self):
        return self.__stories_tab

    def get_tasks_tab(self):
        return self.__tasks_tab

    def get_comments_tab(self):
        return self.__comments_tab

    def get_workspaces_tab(self):
        return self.__workspaces_tab

    def get_accounts_tab(self):
        return self.__accounts_tab

    def set_request_status(self, value):
        self.__status.setText('Status: ' + value)
