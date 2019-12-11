import os

import math
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import *
from designer.base import QAction, QIcon, QLabel, QObject, pyqtSignal
from designer.detectionCNV import DetectionCNV


class ConFigNavigation(QObject):
    def __init__(self, navigation):
        super(ConFigNavigation,self).__init__()
        self.navigation = navigation
        self.detailFrame = self.navigation.parent.selectInputFile
        self.settingFrame=self.navigation.parent.mainContent
        self.mainContents = self.navigation.parent.mainContents
        self.resultChrFrame=self.navigation.parent.resultChr
        self.bindConnect()

    def bindConnect(self):
        self.navigation.left_label_2.clicked.connect(self.goInputFile)
        self.navigation.left_label_1.clicked.connect(self.goSetting)
        self.settingFrame.next_button.clicked.connect(self.goInputFile)
        self.detailFrame.pre_button.clicked.connect(self.goSetting)
        self.navigation.left_label_3.clicked.connect(self.goResultChr)

    def goInputFile(self):
        self.mainContents.setCurrentIndex(1)
        # self.navigation.left_label_2.setCheckabed(True)

    def goSetting(self):
        self.mainContents.setCurrentIndex(0)
        # self.navigation.left_label_1.setCheckabed(True)

    def goResultChr(self):
        self.mainContents.setCurrentIndex(3)


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

class ConfigResultChr(QObject):
    chrLength = [248956422, 242193529, 198295559, 190214555, 181538259, 170805979, 159345973, 145138636, 138394717,
                 133797422, 135086622, 133275309, 114364328, 107043718, 101991189, 90338345, 83257441, 80373285,
                 58617616, 64444167, 46709983, 50818468, 156040895, 57227415]
    def __init__(self,mainContent):
        super(ConfigResultChr,self).__init__()
        self.mainContent=mainContent
        self.detectionCNV = DetectionCNV()
        self.bind()

    def bind(self):
        self.mainContent.searchGo.clicked.connect(self.search)
        self.searchLine=self.mainContent.searchLine
        self.cnvShow=self.mainContent.cnvShowLabel
        self.chrLable=self.mainContent.chrLable
        self.chrLable.goSignal.connect(self.regionShow)

    def search(self):
        if self.searchLine.text()!="":
            self.region=self.searchLine.text()
            pos1=self.region.find(':')
            pos2=self.region.find('-')
            chr=int(self.region[3:pos1].strip())-1
            start=int(self.region[pos1+1:pos2].strip())
            end=int(self.region[pos2+1:].strip())
            self.chrLable.x0= int(start * 580/self.chrLength[chr])
            self.chrLable.x1 = math.ceil(end * 580/self.chrLength[chr])
            self.chrLable.goButtonEvent()
            self.regionShow([chr,start,end])


    def regionShow(self,searchRegion):
        searchRegionStr="chr"+str(searchRegion[0]+1)+": "+str(searchRegion[1])+" - "+str(searchRegion[2])
        self.searchLine.setText(searchRegionStr)
        region = self.detectionCNV.dealSearchRegion(searchRegion)
        self.cnvShow.setPixmap(QPixmap("G:\\refMean.png"))
        self.cnvShow.setScaledContents(True)






