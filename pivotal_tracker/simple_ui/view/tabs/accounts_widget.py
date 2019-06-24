from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit
from pivotal_tracker.simple_ui.view.chuchusmote_splitter import ChuchusmoteSplitter


class AccountsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__get_button = QPushButton('GET')
        self.__get_summary_button = QPushButton('GET SUMMARY')
        self.__id = QLineEdit()
        self.__split_main_window()

    def __split_main_window(self):
        max_height = 900
        factor = 30
        v_widgets = [
            (QLabel("ID"), factor),
            (self.__id, factor),
            (QLabel("GET"), factor),
            (self.__get_button, factor),
            (self.__get_summary_button, factor),
            (QWidget(), max_height-5*factor)
        ]
        vertical = ChuchusmoteSplitter(v_widgets).vertical_split()
        box = QHBoxLayout(self)
        box.addWidget(vertical)
        self.setLayout(box)

    def get_get_button(self):
        return self.__get_button

    def get_get_summary_button(self):
        return self.__get_summary_button

    def get_id(self):
        return self.__id.text()
