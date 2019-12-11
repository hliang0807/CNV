from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# 一个用于继承的类，方便多次调用。
class ScrollArea(QScrollArea):
    """包括一个ScrollArea做主体承载一个QFrame的基础类。"""
    scrollDown = pyqtSignal()

    def __init__(self, parent=None):
        super(ScrollArea, self).__init__()
        self.parent = parent
        self.frame = QFrame()
        self.frame.setObjectName('frame')
        # 用于发出scroll滑到最底部的信号。
        self.verticalScrollBar().valueChanged.connect(self.sliderPostionEvent)

        self.setWidgetResizable(True)

        self.setWidget(self.frame)

    def noInternet(self):
        # 设置没有网络的提示。
        self.noInternetLayout = QGridLayout()
        self.setLayout(self.mainLayout)

        self.Tip = QLabel("您已进入没有网络的异次元，打破次元壁 →", self)
        self.TipButton = QPushButton("打破次元壁", self)
        self.TipButton.setObjectName("TipButton")

        self.TipLayout = QHBoxLayout()
        self.TipLayout.addWidget(self.Tip)
        self.TipLayout.addWidget(self.TipButton)

        # self.indexAllSings.setLayout(self.TipLayout)

        self.noInternetLayout.addLayout(self.TipLayout, 0, 0, Qt.AlignCenter | Qt.AlignTop)

        self.frame.setLayout(self.noInternetLayout)

    def sliderPostionEvent(self):
        if self.verticalScrollBar().value() == self.verticalScrollBar().maximum():
            self.scrollDown.emit()

    def maximumValue(self):
        return self.verticalScrollBar().maximum()


class TableWidget(QTableWidget):
    def __init__(self, count, headerLables):
        super(TableWidget, self).__init__()
        self.setColumnCount(count)
        self.setHorizontalHeaderLabels(headerLables)

        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setVisible(False)
        self.setShowGrid(False)
        self.setAlternatingRowColors(True)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

    def setColumnWidths(self, widths: dict):
        for key in widths:
            self.setColumnWidth(key, widths[key])











