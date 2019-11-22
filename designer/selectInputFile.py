from designer.base import (ScrollArea, QLabel, QFrame, QVBoxLayout, QPushButton, QHBoxLayout, QTableWidget,
                  QAbstractItemView)


class SelectInputFile(ScrollArea):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent



    def setMusicTable(self):
        self.singsTable = QTableWidget()
