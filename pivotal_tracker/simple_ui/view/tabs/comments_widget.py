from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit, \
    QCheckBox, QTextEdit
from pivotal_tracker.simple_ui.view.chuchusmote_splitter import ChuchusmoteSplitter
from json import loads


class CommentsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__get_button = QPushButton('GET')
        self.__put_button = QPushButton('PUT')
        self.__post_button = QPushButton('POST')
        self.__delete_button = QPushButton('DELETE')
        self.__id = QLineEdit()
        self.__project_id = QLineEdit()
        self.__story_id = QLineEdit()
        self.__raw_put = QCheckBox()
        self.__from_options = QCheckBox()
        self.__from_options.setChecked(True)
        self.__raw_put.clicked.connect(self.__onchange_raw_option)
        self.__from_options.clicked.connect(self.__onchange_from_option)
        self.__raw_widget = QTextEdit()
        self.__new_name = QLineEdit()
        self.__split_main_window()
        self.__onchange_from_option()

    def __onchange_raw_option(self):
        if self.__raw_put.isChecked():
            self.__from_options.setChecked(False)
        else:
            self.__from_options.setChecked(True)
        self.__raw_widget.setHidden(False)
        self.__all_put_options.setHidden(True)

    def __onchange_from_option(self):
        if self.__from_options.isChecked():
            self.__raw_put.setChecked(False)
        else:
            self.__raw_put.setChecked(True)
        self.__raw_widget.setHidden(True)
        self.__all_put_options.setHidden(False)

    def __split_main_window(self):
        max_height = 900
        factor = 30
        from_options = ChuchusmoteSplitter().side_by_side(QLabel('From options'),
                                                          self.__from_options)
        raw_options = ChuchusmoteSplitter().side_by_side(QLabel('Raw'), self.__raw_put)
        h_put_raw_options = {
            (raw_options, 300),
            (from_options, 300),
        }
        horizontal_options = ChuchusmoteSplitter(h_put_raw_options).horizontal_split()
        put_name = ChuchusmoteSplitter().side_by_side(QLabel('New text'), self.__new_name)
        v_from_options = {
            (put_name, 1.5*factor),
            (QWidget(), 1.5*factor),
            (QWidget(), 1.5*factor),
        }
        v_from_options = ChuchusmoteSplitter(v_from_options).vertical_split()
        self.__all_put_options = v_from_options
        put_post = ChuchusmoteSplitter().side_by_side(self.__post_button, self.__put_button)
        v_widgets = [
            (QLabel("ID"), factor),
            (self.__id, factor),
            (QLabel("Story ID"), factor),
            (self.__story_id, factor),
            (QLabel("Project ID"), factor),
            (self.__project_id, factor),
            (QLabel("GET"), factor),
            (self.__get_button, factor),
            (QLabel("DELETE"), factor),
            (self.__delete_button, factor),
            (QWidget(), factor),
            (QLabel("PUT - POST Options"), factor),
            (horizontal_options, factor),
            (self.__raw_widget, 3*factor),
            (self.__all_put_options, 3*factor),
            (put_post, factor),
            (QWidget(), max_height-20*factor)
        ]
        vertical = ChuchusmoteSplitter(v_widgets).vertical_split()
        box = QHBoxLayout(self)
        box.addWidget(vertical)
        self.setLayout(box)

    def get_get_button(self):
        return self.__get_button

    def get_put_button(self):
        return self.__put_button

    def get_post_button(self):
        return self.__post_button

    def get_delete_button(self):
        return self.__delete_button

    def get_id(self):
        return self.__id.text()

    def get_project_id(self):
        return self.__project_id.text()

    def get_story_id(self):
        return self.__story_id.text()

    def get_put_post_data(self):
        data = {}
        if self.__from_options.isChecked():
            if self.__new_name.text():
                data["text"] = self.__new_name.text()
        elif self.__raw_put.isChecked():
            data = loads(self.__raw_widget.toPlainText())
        return data
