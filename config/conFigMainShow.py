
from designer.base import QAction, QMenu, checkFolder, QIcon, QLabel, QObject, RequestThread, QTableWidgetItem, QCursor, pyqtSignal

class ConFigNavigation(QObject):
    def __init__(self, navigation):
        super(ConFigNavigation,self).__init__()
        self.navigation = navigation
        self.detailFrame = self.navigation.parent.selectInputFile
        self.mainContents = self.navigation.parent.mainContents
        self.bindConnect()

    def bindConnect(self):
        self.navigation.left_label_2.clicked.connect(self.goInputFile)
        self.navigation.left_label_1.clicked.connect(self.goSetting)

    def goInputFile(self):
        self.mainContents.setCurrentIndex(1)

    def goSetting(self):
        self.mainContents.setCurrentIndex(0)