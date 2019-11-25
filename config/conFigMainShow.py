import os
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog

from designer.base import QAction, QMenu, checkFolder, QIcon, QLabel, QObject, RequestThread, QTableWidgetItem, QCursor, pyqtSignal

class ConFigNavigation(QObject):
    def __init__(self, navigation):
        super(ConFigNavigation,self).__init__()
        self.navigation = navigation
        self.detailFrame = self.navigation.parent.selectInputFile
        self.settingFrame=self.navigation.parent.mainContent
        self.mainContents = self.navigation.parent.mainContents
        self.bindConnect()

    def bindConnect(self):
        self.navigation.left_label_2.clicked.connect(self.goInputFile)
        self.navigation.left_label_1.clicked.connect(self.goSetting)
        self.settingFrame.next_button.clicked.connect(self.goInputFile)
        self.detailFrame.pre_button.clicked.connect(self.goSetting)

    def goInputFile(self):
        self.mainContents.setCurrentIndex(1)
        # self.navigation.left_label_2.setCheckabed(True)

    def goSetting(self):
        self.mainContents.setCurrentIndex(0)
        # self.navigation.left_label_1.setCheckabed(True)


class ConfigInputFrame(QObject):
    def __init__(self,selectInputFile):
        super(ConfigInputFrame,self).__init__()
        self.selectInputFile=selectInputFile
        self.getFile()

    def getFile(self):
        self.selectInputFile.file_button1.clicked.connect(self.loadPath1)
        self.selectInputFile.file_button2.clicked.connect(self.loadPath2)
        self.selectInputFile.file_button3.clicked.connect(self.loadPath3)
        self.selectInputFile.file_button4.clicked.connect(self.loadPath4)

    def loadPath1(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            filePath = dialog.selectedFiles()[0]
            filename=os.path.basename(filePath)
            self.selectInputFile.file_path1.setText(filename)
            self.refPathFile=filePath

    def loadPath2(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            filePath = dialog.selectedFiles()[0]
            filename=os.path.basename(filePath)
            self.selectInputFile.file_path2.setText(filename)
            self.testFile=filePath

    def loadPath3(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            filePath = dialog.selectedFiles()[0]
            filename=os.path.basename(filePath)
            self.selectInputFile.file_path3.setText(filename)
            self.exonFile=filePath

    def loadPath4(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            filePath = dialog.selectedFiles()[0]
            filename=os.path.basename(filePath)
            self.selectInputFile.file_path4.setText(filename)
            self.gcFile=filePath



class ConfigSettingFrame(QObject):
    def __init__(self,mainContent):
        super(ConfigSettingFrame,self).__init__()
        self.mainContent=mainContent
        self.noticMess()

    def noticMess(self):
        self.mainContent.right_lable1.setToolTip("MAPQ值越大，出错率越低，比对质量越好，一般选20")
        self.mainContent.right_lable2.setToolTip("最小的外显子长度，低于设定值的外显子会被过滤掉")
        self.mainContent.right_lable3.setToolTip("gc含量的下限，gc含量低于设定值的外显子会被过滤掉")
        self.mainContent.right_lable4.setToolTip("gc含量的上限，gc含量高于设定值的外显子会被过滤掉")
        self.mainContent.right_lable5.setToolTip("正常样本外显子上平均reads count的下限，低于设定值的外显子会被过滤掉")
        self.mainContent.right_lable6.setToolTip("判断测试样本一个外显子reads count是否异常的阈值")
        self.mainContent.right_lable7.setToolTip("选取和测试样本距离最近的正常样本作为ref样本集")
        self.mainContent.right_lable8.setToolTip("一个CNV区域最少包含的外显子个数")
        self.mainContent.right_lable9.setToolTip("进程池的进程数")



