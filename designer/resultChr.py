from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math
from designer.myLabel import MyLabel
from designer.base import ScrollArea


class ResultChr(ScrollArea):
    def __init__(self, parent=None):
        super(ResultChr, self).__init__()
        self.parent = parent
        self.cnvShow_widget = QWidget()
        self.setWidget(self.cnvShow_widget)
        self.setWidgetResizable(True)
        self.setObjectName("cnvShow")
        with open("QSS/resultChr.qss", 'r', encoding='utf-8') as f:
            self.style = f.read()
            self.setStyleSheet(self.style)
            self.cnvShow_widget.setStyleSheet(self.style)
        self.setLabels()
        self.setLayouts()

    def setLabels(self):
        self.searchLable=QLabel("请输入基因组区域")
        self.searchLable.setObjectName("searchLable")
        # self.searchCB=QComboBox()
        # self.searchCB.setObjectName("searchComboBox")
        # self.searchCB.addItem("chr1")
        # self.searchCB.addItem("chr2")
        # self.searchCB.addItem("chr3")
        # self.searchCB.addItem("chr4")
        # self.searchCB.addItem("chr5")
        # self.searchCB.addItem("chr6")
        # self.searchCB.addItem("chr7")
        # self.searchCB.addItem("chr8")
        # self.searchCB.addItem("chr9")
        # self.searchCB.addItem("chr10")
        # self.searchCB.addItem("chr11")
        # self.searchCB.addItem("chr12")
        # self.searchCB.addItem("chr13")
        # self.searchCB.addItem("chr14")
        # self.searchCB.addItem("chr15")
        # self.searchCB.addItem("chr16")
        # self.searchCB.addItem("chr17")
        # self.searchCB.addItem("chr18")
        # self.searchCB.addItem("chr19")
        # self.searchCB.addItem("chr20")
        # self.searchCB.addItem("chr21")
        # self.searchCB.addItem("chr22")
        # self.searchCB.addItem("chrX")
        # self.searchCB.addItem("chrY")
        self.searchLine = QLineEdit()
        self.searchLine.setObjectName("searchLine")
        self.searchGo=QPushButton("go")
        self.searchGo.setObjectName("searchGo")

        self.chrNumLabel=QLabel("chr1")
        self.chrNumLabel.setObjectName("chrNumLabel")
        self.chrLable=MyLabel()
        self.chrLable.setFixedSize(580,25)
        chrImg=QImage("resource/chr1.png")
        self.chrLable.setPixmap(QPixmap.fromImage(chrImg.scaled(self.chrLable.width(),self.chrLable.height(),
                                                                Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        self.chrLable.setScaledContents(True)

        self.cnvShowLabel=QLabel()
        self.cnvShowLabel.setPixmap(QPixmap(""))
        self.cnvNumLabel = QLabel()
        self.cnvNumLabel.setPixmap(QPixmap(""))

        self.geneMessLabel = QLabel("基因名称")
        self.geneText= QTextEdit()
        self.geneText.setObjectName("geneText")

        self.space1=QLabel()
        self.space2 = QLabel()
        self.space3 = QLabel()


    def setLayouts(self):
        self.mainLayout = QGridLayout(self.cnvShow_widget)
        self.region_layout=QGridLayout()
        self.region_widget = QWidget()
        self.region_widget.setLayout(self.region_layout)
        self.region_layout.addWidget(self.searchLable,0,2,1,1)
        self.region_layout.addWidget(self.searchLine, 0, 3, 1, 1)
        self.region_layout.addWidget(self.searchGo, 0, 4, 1, 1)
        self.region_layout.addWidget(self.space2, 0, 5, 1, 1)

        self.region_layout.addWidget(self.chrNumLabel, 1, 0, 1, 1)
        self.region_layout.addWidget(self.chrLable,1,1,1,5)

        self.region_layout.addWidget(self.geneMessLabel, 2, 0, 1, 2)
        self.region_layout.addWidget(self.geneText,2,2,1,3)

        self.region_layout.addWidget(self.cnvShowLabel, 3,0,1,5)
        self.region_layout.addWidget(self.cnvNumLabel, 4,0,1,5)
        self.region_layout.addWidget(self.space1,1,5,1,1)


        self.region_layout.setColumnStretch(0, 0.5)
        self.region_layout.setColumnStretch(1, 0.5)
        self.region_layout.setColumnStretch(2, 1)
        self.region_layout.setColumnStretch(3, 2)
        self.region_layout.setColumnStretch(4, 0.5)
        self.region_layout.setColumnStretch(5, 1)
        self.region_layout.setRowStretch(0, 1)
        self.region_layout.setRowStretch(1, 1)
        self.region_layout.setRowStretch(2, 1)
        self.region_layout.setRowStretch(3, 4)
        self.mainLayout.addWidget(self.region_widget, 0, 0, 3, 6)




