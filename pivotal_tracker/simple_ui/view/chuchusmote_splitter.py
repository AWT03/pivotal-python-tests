#
# @chuchusmote_splitter.py Copyright (c) 2019 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from PyQt5.QtWidgets import QSplitter
from PyQt5.QtCore import Qt


# This class simplifies the split of a QWidget
class ChuchusmoteSplitter:
    # widget data is a tuple that contains tuples with widget and size
    # [ [widget_1, size], [widget_2, size], ..., [widget_n, size_n] ]
    def __init__(self, widget_data=[]):
        self.widget_data = widget_data

    # This method returns a vertical split
    def vertical_split(self):
        vertical = QSplitter(Qt.Vertical)
        weights = []
        for widget in self.widget_data:
            vertical.addWidget(widget[0])
            weights.append(widget[1])
        vertical.setSizes(weights)
        return vertical

    # This method returns a horizontal split
    def horizontal_split(self):
        horizontal = QSplitter(Qt.Horizontal)
        weights = []
        for widget in self.widget_data:
            horizontal.addWidget(widget[0])
            weights.append(widget[1])
        horizontal.setSizes(weights)
        return horizontal

    @staticmethod
    def side_by_side(widget1, widget2):
        horizontal = [
            (widget1, 100),
            (widget2, 100)
        ]
        return ChuchusmoteSplitter(horizontal).horizontal_split()
