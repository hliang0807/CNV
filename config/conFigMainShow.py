import os
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from designer.detectionCNV import DetectionCNV
chrLength = [248956422, 242193529, 198295559, 190214555, 181538259, 170805979, 159345973, 145138636, 138394717,
                 133797422, 135086622, 133275309, 114364328, 107043718, 101991189, 90338345, 83257441, 80373285,
                 58617616, 64444167, 46709983, 50818468, 156040895, 57227415]


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
        self.mainContents.setCurrentIndex(2)


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


class ConfigChooseChr(QObject):
    def __init__(self,mainContent):
        super(ConfigChooseChr,self).__init__()
        self.mainContent=mainContent
        self.geneChr = self.mainContent.parent.detectionCNV.geneChr
        self.mainContents = self.mainContent.parent.mainContents
        self.chrLable = self.mainContent.parent.resultChr.chrLable
        self.chrNumLabel=self.mainContent.parent.resultChr.chrNumLabel


        self.configResultChr = self.mainContent.parent.configResultChr
        self.bindConnect()


    def bindConnect(self):
        self.mainContent.chr1.clicked.connect(self.goChr1)
        self.mainContent.chr2.clicked.connect(self.goChr2)
        self.mainContent.chr3.clicked.connect(self.goChr3)
        self.mainContent.chr4.clicked.connect(self.goChr4)
        self.mainContent.chr5.clicked.connect(self.goChr5)
        self.mainContent.chr6.clicked.connect(self.goChr6)
        self.mainContent.chr7.clicked.connect(self.goChr7)
        self.mainContent.chr8.clicked.connect(self.goChr8)
        self.mainContent.chr9.clicked.connect(self.goChr9)
        self.mainContent.chr10.clicked.connect(self.goChr10)
        self.mainContent.chr11.clicked.connect(self.goChr11)
        self.mainContent.chr12.clicked.connect(self.goChr12)
        self.mainContent.chr13.clicked.connect(self.goChr13)
        self.mainContent.chr14.clicked.connect(self.goChr14)
        self.mainContent.chr15.clicked.connect(self.goChr15)
        self.mainContent.chr16.clicked.connect(self.goChr16)
        self.mainContent.chr17.clicked.connect(self.goChr17)
        self.mainContent.chr18.clicked.connect(self.goChr18)
        self.mainContent.chr19.clicked.connect(self.goChr19)
        self.mainContent.chr20.clicked.connect(self.goChr20)
        self.mainContent.chr21.clicked.connect(self.goChr21)
        self.mainContent.chr22.clicked.connect(self.goChr22)
        self.mainContent.chrX.clicked.connect(self.goChrX)
        self.mainContent.chrY.clicked.connect(self.goChrY)

    def search(self,region):
        chr=int(region[0])-1
        start=region[1]
        end=region[2]
        self.chrLable.x0= int(start * 580/chrLength[chr])
        self.chrLable.x1 = math.ceil(end * 580/chrLength[chr])
        self.chrLable.chrNum=chr
        self.chrLable.goButtonEvent()
        self.configResultChr.regionShow([chr,start,end])

    def setResultChr(self,chrNum):
        region = self.geneChr[chrNum-1][len(self.geneChr[chrNum-1]) // 3]
        self.search(region)
        self.chrNumLabel.setText("chr"+str(chrNum))
        chrImg = QImage("resource/chr"+str(chrNum)+".png")
        self.chrLable.setPixmap(QPixmap.fromImage(chrImg.scaled(self.chrLable.width(), self.chrLable.height(),
                                                                Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        self.mainContents.setCurrentIndex(3)

    def goChr1(self):
        self.setResultChr(1)


    def goChr2(self):
        self.setResultChr(2)

    def goChr3(self):
        self.setResultChr(3)

    def goChr4(self):
        self.setResultChr(4)

    def goChr5(self):
        self.setResultChr(5)

    def goChr6(self):
        self.setResultChr(6)

    def goChr7(self):
        self.setResultChr(7)

    def goChr8(self):
        self.setResultChr(8)

    def goChr9(self):
        self.setResultChr(9)

    def goChr10(self):
        self.setResultChr(10)

    def goChr11(self):
        self.setResultChr(11)

    def goChr12(self):
        self.setResultChr(12)

    def goChr13(self):
        self.setResultChr(13)

    def goChr14(self):
        self.setResultChr(14)

    def goChr15(self):
        self.setResultChr(15)

    def goChr16(self):
        self.setResultChr(16)

    def goChr17(self):
        self.setResultChr(17)

    def goChr18(self):
        self.setResultChr(18)

    def goChr19(self):
        self.setResultChr(19)

    def goChr20(self):
        self.setResultChr(20)

    def goChr21(self):
        self.setResultChr(21)

    def goChr22(self):
        self.setResultChr(22)

    def goChrX(self):
        pass
        # self.setResultChr(23)

    def goChrY(self):
        pass
        # self.setResultChr(24)


class ConfigResultChr(QObject):
    def __init__(self,mainContent):
        super(ConfigResultChr,self).__init__()
        self.mainContent=mainContent
        self.detectionCNV = self.mainContent.parent.detectionCNV
        self.searchLine = self.mainContent.searchLine
        self.cnvShow = self.mainContent.cnvShowLabel
        self.cnvNum = self.mainContent.cnvNumLabel
        self.chrLable = self.mainContent.chrLable
        self.geneText = self.mainContent.geneText
        self.bind()

    def bind(self):
        self.mainContent.searchGo.clicked.connect(self.search)
        self.chrLable.goSignal.connect(self.regionShow)

    def search(self):
        if self.searchLine.text()!="":
            self.region=self.searchLine.text()
            pos1=self.region.find(':')
            pos2=self.region.find('-')
            chr=int(self.region[3:pos1].strip())-1
            start=int(self.region[pos1+1:pos2].strip())
            end=int(self.region[pos2+1:].strip())
            self.chrLable.x0= round(start * 580/chrLength[chr])
            self.chrLable.x1 = round(end * 580/chrLength[chr])
            self.chrLable.goButtonEvent()
            self.regionShow([chr,start,end])


    def regionShow(self,searchRegion):
        searchRegionStr="chr"+str(searchRegion[0]+1)+": "+str(searchRegion[1])+" - "+str(searchRegion[2])
        self.searchLine.setText(searchRegionStr)
        region, geneRegion = self.detectionCNV.dealSearchRegion(searchRegion)
        width=600
        hight=450
        if len(region)>0:
            self.cnvShow.setPixmap(QPixmap.fromImage(QImage("temp/refMean.png").
                                                      scaled(width, hight, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
            self.cnvShow.setScaledContents(True)
            self.cnvNum.setPixmap(QPixmap.fromImage(QImage("temp/exonCNV.png").
                                                    scaled(width, hight, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
            self.cnvNum.setScaledContents(True)
        else:
            self.cnvShow.setPixmap(QPixmap(""))
            self.cnvNum.setPixmap(QPixmap(""))
        geneText=""
        for cur in geneRegion:
            geneText+=cur[3]+"  "
        self.geneText.setText(geneText)







