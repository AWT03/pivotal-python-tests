import sys
from PyQt5.QtWidgets import QApplication
from pivotal_tracker.simple_ui.controller.controller import Controller
from pivotal_tracker.simple_ui.view.view import View


# This UI can be used as some quick testing of the API
if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    controller = Controller(view)
    sys.exit(app.exec())
