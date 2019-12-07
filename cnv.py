import os
import sys
import os.path
import asyncio
import logging

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
# widgets
from config.conFigMainShow import ConFigNavigation, ConfigInputFrame, ConfigSettingFrame, ConfigResultChr
from designer.base import (QApplication, cacheFolder, QDialog, QFrame, QHBoxLayout, HBoxLayout, QIcon, QLabel,
                           QListWidget, QListWidgetItem,
                           QPushButton, PicLabel, QScrollArea, ScrollArea, Qt, QTabWidget, TableWidget, QVBoxLayout,
                           VBoxLayout,
                           QWidget)
from designer.chooseChr import ChooseChr
from designer.resultChr import ResultChr
from designer.selectInputFile import SelectInputFile
from designer.systemTray import SystemTray


# 用于承载整个界面。所有窗口的父窗口，所有窗口都可以在父窗口里找到索引。
class Window(QMainWindow):
    """Window 承载整个界面。"""

    def __init__(self):
        super(Window, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName('MainWindow')
        self.setWindowTitle("拷贝数变异检测系统")
        self.resize(800, 600)
        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_layout = QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.navigation = Navigation(self)
        self.mainContent = MainContent(self)
        self.selectInputFile = SelectInputFile(self)
        self.resultChr = ResultChr(self)
        self.chooseChr = ChooseChr(self)

        self.mainContents = QTabWidget()
        self.mainContents.tabBar().setObjectName("mainTab")

        # 加载tab设置。
        self.setContents()
        # 设置布局。
        self.setLayouts()
        # 注册功能。
        self.configFeatures()

        with open('QSS/window.qss', 'r') as f:
            self.setStyleSheet(f.read())

    # 布局。
    def setContents(self):
        """设置tab界面。"""
        # 将需要切换的窗口做成Tab，并隐藏tabBar，这样方便切换，并且可以做前进后退功能。
        self.mainContents.addTab(self.mainContent, '')
        self.mainContents.addTab(self.selectInputFile, '')
        self.mainContents.addTab(self.chooseChr, '')
        self.mainContents.addTab(self.resultChr, '')
        self.mainContents.setCurrentIndex(3)

    def setLayouts(self):
        self.main_layout.addWidget(self.navigation, 0, 0, 12, 2)
        self.main_layout.addWidget(self.mainContents, 0, 2, 12, 8)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setHorizontalSpacing(0)
        self.setCentralWidget(self.main_widget)

    # 注册所有功能。
    def configFeatures(self):
        self.navigationConfig = ConFigNavigation(self.navigation)
        self.configInputFrame = ConfigInputFrame(self.selectInputFile)
        self.configSetting = ConfigSettingFrame(self.mainContent)
        self.configResultChr=ConfigResultChr(self.resultChr)


# 左侧的导航栏
class Navigation(QScrollArea):
    def __init__(self, parent=None):
        super(Navigation, self).__init__(parent)
        self.parent = parent
        self.left_widget = QWidget()
        self.setWidget(self.left_widget)
        self.setWidgetResizable(True)
        self.setObjectName('left_widget')

        with open('QSS/navigation.qss', 'r') as f:
            style = f.read()
            self.setStyleSheet(style)
            self.left_widget.setStyleSheet(style)

        # 包括显示信息：
        self.setLabels()
        self.setLayouts()

    # 布局
    def setLabels(self):
        self.left_label_1 = QPushButton("参数设置")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QPushButton("选择文件")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QPushButton("拷贝数变异")
        self.left_label_3.setObjectName('left_label')
        self.left_label_4 = QPushButton("反馈与帮助")
        self.left_label_4.setObjectName('left_label')
        self.left_label_5 = QLabel()
        self.left_label_5.setObjectName('left_label')


        # self.left_label_1.setCheckable(True)
        # self.left_label_1.setChecked(True)
        # self.left_label_1.setAutoExclusive(True)
        # self.left_label_2.setAutoExclusive(True)
        # self.left_label_3.setAutoExclusive(True)
        # self.left_label_2.setCheckable(True)
        # self.left_label_3.setCheckable(True)

    def setLayouts(self):
        """设置布局。"""
        self.left_layout = QGridLayout(self.left_widget)  # 创建左侧部件的网格布局层
        self.left_layout.addWidget(self.left_label_1, 0, 0, 1, 2)
        self.left_layout.addWidget(self.left_label_2, 1, 0, 1, 2)
        self.left_layout.addWidget(self.left_label_3, 2, 0, 1, 2)
        self.left_layout.addWidget(self.left_label_4, 4, 0, 1, 2)
        self.left_layout.addWidget(self.left_label_5, 5, 0, 1, 2)
        self.left_layout.setRowStretch(0, 2)
        self.left_layout.setRowStretch(1, 2)
        self.left_layout.setRowStretch(2, 2)
        self.left_layout.setRowStretch(3, 7)
        self.left_layout.setRowStretch(4, 2)
        self.left_layout.setRowStretch(5, 1)


# 主要内容区
class MainContent(ScrollArea):

    def __init__(self, parent=None):
        """主内容区"""
        super(MainContent, self).__init__()
        self.parent = parent
        self.right_widget = QWidget()
        self.setWidget(self.right_widget)
        self.setWidgetResizable(True)
        self.setObjectName("MainContent")

        with open("QSS/mainContent.qss", 'r', encoding='utf-8') as f:
            self.style = f.read()
            self.setStyleSheet(self.style)
            self.right_widget.setStyleSheet(self.style)

        self.setLabels()
        self.setLayouts()

        # 布局

    def setLabels(self):
        self.right_lable1 = QPushButton("mapping quality")
        self.right_lable1.setObjectName('right_lable')
        self.right_lable2 = QPushButton("外显子长度")
        self.right_lable2.setObjectName('right_lable')
        self.right_lable3 = QPushButton("gc含量下限(%)")
        self.right_lable3.setObjectName('right_lable')
        self.right_lable4 = QPushButton("gc含量上限(%)")
        self.right_lable4.setObjectName('right_lable')
        self.right_lable5 = QPushButton("read count")
        self.right_lable5.setObjectName('right_lable')
        self.right_lable6 = QPushButton("z-score阈值")
        self.right_lable6.setObjectName('right_lable')
        self.right_lable7 = QPushButton("ref样本数")
        self.right_lable7.setObjectName('right_lable')
        self.right_lable8 = QPushButton("合并外显子")
        self.right_lable8.setObjectName('right_lable')
        self.right_lable9 = QPushButton("进程数量")
        self.right_lable9.setObjectName('right_lable')


        self.right_line1 = QLineEdit()
        self.right_line1.setPlaceholderText("20(default)")
        self.right_line1.setValidator(QtGui.QIntValidator())
        self.right_line1.setObjectName('right_line')
        self.right_line2 = QLineEdit()
        self.right_line2.setPlaceholderText("20(default)")
        self.right_line2.setValidator(QtGui.QIntValidator())
        self.right_line2.setObjectName('right_line')
        self.right_line3 = QLineEdit()
        self.right_line3.setPlaceholderText("10(default)")
        self.right_line3.setValidator(QtGui.QIntValidator())
        self.right_line3.setObjectName('right_line')
        self.right_line4 = QLineEdit()
        self.right_line4.setPlaceholderText("90(default)")
        self.right_line4.setValidator(QtGui.QIntValidator())
        self.right_line4.setObjectName('right_line')
        self.right_line5 = QLineEdit()
        self.right_line5.setPlaceholderText("20(default)")
        self.right_line5.setValidator(QtGui.QIntValidator())
        self.right_line5.setObjectName('right_line')
        self.right_line6 = QLineEdit()
        self.right_line6.setPlaceholderText("3(default)")
        self.right_line6.setValidator(QtGui.QIntValidator())
        self.right_line6.setObjectName('right_line')
        self.right_line7 = QLineEdit()
        self.right_line7.setPlaceholderText("50(default)")
        self.right_line7.setValidator(QtGui.QIntValidator())
        self.right_line7.setObjectName('right_line')
        self.right_line8 = QLineEdit()
        self.right_line8.setPlaceholderText("3(default)")
        self.right_line8.setValidator(QtGui.QIntValidator())
        self.right_line8.setObjectName('right_line')
        self.right_line9 = QLineEdit()
        self.right_line9.setPlaceholderText("1(default)")
        self.right_line9.setValidator(QtGui.QIntValidator())
        self.right_line9.setObjectName('right_line')

        self.space1 = QLabel()
        self.space2 = QLabel()
        self.space3 = QLabel()
        self.space4 = QLabel()
        self.space5 = QLabel()
        self.space6 = QLabel()
        self.space7 = QLabel()
        self.space8 = QLabel()
        self.space9 = QLabel()
        self.space10 = QLabel()
        self.space11 = QLabel()
        self.space12 = QLabel()

        self.next_button = QPushButton("下一步")
        self.next_button.setObjectName('next_button')

    # 定义布局
    def setLayouts(self):
        self.mainLayout = QGridLayout(self.right_widget)
        self.right_label_layout = QGridLayout()
        self.right_label_widget = QWidget()
        self.right_label_widget.setLayout(self.right_label_layout)
        self.right_label_layout.addWidget(self.right_lable1, 1, 1, 1, 1)
        self.right_label_layout.addWidget(self.right_lable2, 3, 1, 1, 1)
        self.right_label_layout.addWidget(self.right_lable3, 5, 1, 1, 1)
        self.right_label_layout.addWidget(self.right_lable4, 7, 1, 1, 1)
        self.right_label_layout.addWidget(self.right_lable5, 9, 1, 1, 1)
        self.right_label_layout.addWidget(self.right_lable6, 11, 1, 1, 1)
        self.right_label_layout.addWidget(self.right_lable7, 13, 1, 1, 1)
        self.right_label_layout.addWidget(self.right_lable8, 15, 1, 1, 1)
        self.right_label_layout.addWidget(self.right_lable9, 17, 1, 1, 1)

        self.right_label_layout.addWidget(self.right_line1, 1, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line2, 3, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line3, 5, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line4, 7, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line5, 9, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line6, 11, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line7, 13, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line8, 15, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line9, 17, 2, 1, 1)
        self.right_label_layout.addWidget(self.next_button, 19, 4, 1, 1)

        self.right_label_layout.addWidget(self.space1, 0, 0, 1, 1)
        self.right_label_layout.addWidget(self.space2, 2, 0, 1, 1)
        self.right_label_layout.addWidget(self.space3, 4, 0, 1, 1)
        self.right_label_layout.addWidget(self.space4, 6, 0, 1, 1)
        self.right_label_layout.addWidget(self.space5, 8, 0, 1, 1)
        self.right_label_layout.addWidget(self.space6, 10, 0, 1, 1)
        self.right_label_layout.addWidget(self.space8, 12, 0, 1, 1)
        self.right_label_layout.addWidget(self.space8, 14, 0, 1, 1)
        self.right_label_layout.addWidget(self.space9, 16, 0, 1, 1)
        self.right_label_layout.addWidget(self.space10, 19, 5, 1, 1)
        self.right_label_layout.addWidget(self.space11, 19, 3, 1, 1)

        self.right_label_layout.setColumnStretch(0, 1)
        self.right_label_layout.setColumnStretch(1, 2)
        self.right_label_layout.setColumnStretch(2, 1)
        self.right_label_layout.setColumnStretch(3, 1)
        self.right_label_layout.setColumnStretch(4, 1.5)
        self.right_label_layout.setColumnStretch(5, 0.5)

        self.right_label_layout.setRowStretch(0, 2)
        self.right_label_layout.setRowStretch(1, 1)
        self.right_label_layout.setRowStretch(2, 1)
        self.right_label_layout.setRowStretch(3, 1)
        self.right_label_layout.setRowStretch(4, 1)
        self.right_label_layout.setRowStretch(5, 1)
        self.right_label_layout.setRowStretch(6, 1)
        self.right_label_layout.setRowStretch(7, 1)
        self.right_label_layout.setRowStretch(8, 1)
        self.right_label_layout.setRowStretch(9, 1)
        self.right_label_layout.setRowStretch(10, 1)
        self.right_label_layout.setRowStretch(11, 1)
        self.right_label_layout.setRowStretch(12, 1)
        self.right_label_layout.setRowStretch(13, 1)
        self.right_label_layout.setRowStretch(14, 1)
        self.right_label_layout.setRowStretch(15, 1)
        self.right_label_layout.setRowStretch(16, 1)
        self.right_label_layout.setRowStretch(17, 1)
        self.right_label_layout.setRowStretch(18, 3)
        self.right_label_layout.setRowStretch(19, 4)

        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.right_label_widget, 1, 1, 19, 4)


def start():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()
