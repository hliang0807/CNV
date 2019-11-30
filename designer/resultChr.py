from designer.base import (ScrollArea, QLabel, QFrame, QVBoxLayout, QPushButton, QHBoxLayout, QTableWidget,
                           QAbstractItemView)
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *

class ResultChr(ScrollArea):
    def __init__(self, parent=None):
        super(ResultChr, self).__init__()
        self.parent = parent
        self.cnvShow_widget = QWidget()
        self.setWidget(self.cnvShow_widget)
        self.setWidgetResizable(True)
        self.setObjectName("cnvShow")
        self.setLabels()
        self.setLayouts()

    def setLabels(self):
        self.searchLable=QLabel("请输入基因组区域")
        self.searchLable.setObjectName("searchLable")
        self.searchCB=QComboBox()
        self.searchCB.addItem("chr1")
        self.searchCB.addItem("chr2")
        self.searchCB.addItem("chr3")
        self.searchCB.addItem("chr4")
        self.searchCB.addItem("chr5")
        self.searchCB.addItem("chr6")
        self.searchCB.addItem("chr7")
        self.searchCB.addItem("chr8")
        self.searchCB.addItem("chr9")
        self.searchCB.addItem("chr10")
        self.searchCB.addItem("chr11")
        self.searchCB.addItem("chr12")
        self.searchCB.addItem("chr13")
        self.searchCB.addItem("chr14")
        self.searchCB.addItem("chr15")
        self.searchCB.addItem("chr16")
        self.searchCB.addItem("chr17")
        self.searchCB.addItem("chr18")
        self.searchCB.addItem("chr19")
        self.searchCB.addItem("chr20")
        self.searchCB.addItem("chr21")
        self.searchCB.addItem("chr22")
        self.searchCB.addItem("chrX")
        self.searchCB.addItem("chrY")

    def setLayout(self):
        pass
