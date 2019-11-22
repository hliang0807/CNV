import os
import sys
import os.path
import asyncio
import logging

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
# widgets
from designer.base import (QApplication, cacheFolder, QDialog, QFrame, QHBoxLayout, HBoxLayout, QIcon, QLabel, QListWidget, QListWidgetItem,
                  QPushButton, PicLabel, QScrollArea, ScrollArea, Qt, QTabWidget, TableWidget, QVBoxLayout, VBoxLayout,
                  QWidget)
from designer.selectInputFile import SelectInputFile
from designer.step2 import Step2
from designer.step3 import Step3
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
        self.step1 = SelectInputFile(self)
        self.step2 = Step2(self)
        self.step3 = Step3(self)

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
        self.mainContents.addTab(self.step1, '')
        self.mainContents.addTab(self.step2, '')
        self.mainContents.addTab(self.step3, '')
        self.mainContents.setCurrentIndex(0)

    def setLayouts(self):
        self.main_layout.addWidget(self.navigation,0,0,12,2)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.mainContents,0,2,12,8)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setHorizontalSpacing(0);
        self.setCentralWidget(self.main_widget)

    # 注册所有功能。
    def configFeatures(self):
        pass



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
        self.left_label_3 = QPushButton("提交")
        self.left_label_3.setObjectName('left_label')
        self.left_label_4= QPushButton("")
        self.left_label_4.setObjectName('left_label')



    def setLayouts(self):
        """设置布局。"""
        self.left_layout = QGridLayout(self.left_widget)  # 创建左侧部件的网格布局层
        self.left_layout.addWidget(self.left_label_1,2,0,2,2)
        self.left_layout.addWidget(self.left_label_2,3,0,3,2)
        self.left_layout.addWidget(self.left_label_3,4,0,4,2)
        self.left_layout.setContentsMargins(0, 0, 0, 0)
        self.left_layout.addWidget(self.left_label_4, 12, 0, 12, 2)




# 主要内容区
class MainContent(ScrollArea):
    # 定义一个滑到了最低部的信号。
    # 方便子控件得知已经滑到了最底部，要做些加载的动作。

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
        self.right_lable2 = QPushButton("外显子大小")
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

        self.right_line1 = QLineEdit("20(default)")
        self.right_line1.setValidator(QtGui.QIntValidator())
        self.right_line1.setObjectName('right_line')
        self.right_line2 = QLineEdit("20(default)")
        self.right_line2.setValidator(QtGui.QIntValidator())
        self.right_line2.setObjectName('right_line')
        self.right_line3 = QLineEdit("10(default)")
        self.right_line3.setValidator(QtGui.QIntValidator())
        self.right_line3.setObjectName('right_line')
        self.right_line4 = QLineEdit("90(default)")
        self.right_line4.setValidator(QtGui.QIntValidator())
        self.right_line4.setObjectName('right_line')
        self.right_line5 = QLineEdit("20(default)")
        self.right_line5.setValidator(QtGui.QIntValidator())
        self.right_line5.setObjectName('right_line')
        self.right_line6 = QLineEdit("3(default)")
        self.right_line6.setValidator(QtGui.QIntValidator())
        self.right_line6.setObjectName('right_line')
        self.right_line7 = QLineEdit("50(default)")
        self.right_line7.setValidator(QtGui.QIntValidator())
        self.right_line7.setObjectName('right_line')
        self.right_line8 = QLineEdit("3(default)")
        self.right_line8.setValidator(QtGui.QIntValidator())
        self.right_line8.setObjectName('right_line')

        self.space_button1=QPushButton()
        self.space_button2 = QPushButton()
        self.space_button3 = QPushButton()
        self.space_button4 = QPushButton()
        self.space_button5 = QPushButton()
        self.space_button6 = QPushButton()
        self.next_button =  QPushButton("next")
        self.next_button.setObjectName('next_button')

    #定义布局
    def setLayouts(self):

        self.mainLayout = QGridLayout(self.right_widget)
        self.right_label_layout=QGridLayout()
        self.right_label_widget = QWidget()
        self.right_label_widget.setLayout(self.right_label_layout)
        self.right_label_layout.addWidget(self.right_lable1,0,1,1,1)
        self.right_label_layout.addWidget(self.right_lable2,1,1,1,1)
        self.right_label_layout.addWidget(self.right_lable3, 2, 1, 1, 1)
        self.right_label_layout.addWidget(self.right_lable4, 3, 1, 1, 1)
        self.right_label_layout.addWidget(self.right_lable5, 4,1,1,1)
        self.right_label_layout.addWidget(self.right_lable6, 5,1,1,1)
        self.right_label_layout.addWidget(self.right_lable7, 6,1,1,1)
        self.right_label_layout.addWidget(self.right_lable8, 7,1,1,1)

        self.right_label_layout.addWidget(self.right_line1, 0, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line2, 1, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line3, 2, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line4, 3, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line5, 4, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line6, 5, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line7, 6, 2, 1, 1)
        self.right_label_layout.addWidget(self.right_line8, 7, 2, 1, 1)

        self.right_label_layout.addWidget(self.next_button, 8, 4, 1, 1)
        self.right_label_layout.setColumnStretch(0,1)
        self.right_label_layout.setColumnStretch(1, 2)
        self.right_label_layout.setColumnStretch(2, 2)
        self.right_label_layout.setColumnStretch(3, 2)
        self.right_label_layout.setColumnStretch(4, 1)
        self.right_label_layout.setVerticalSpacing(30)

        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.right_label_widget,1,1,8,4)



def start():
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()