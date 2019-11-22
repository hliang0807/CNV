from designer.base import (ScrollArea, QLabel, QFrame, QVBoxLayout, QPushButton, QHBoxLayout, QTableWidget,
                  QAbstractItemView)
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *

class SelectInputFile(ScrollArea):
    def __init__(self, parent=None):
        """主内容区"""
        super(SelectInputFile, self).__init__()
        self.parent = parent
        self.inputFile_widget = QWidget()
        self.setWidget(self.inputFile_widget)
        self.setWidgetResizable(True)
        self.setObjectName("InputFile")

        with open("QSS/inputFile.qss", 'r', encoding='utf-8') as f:
            self.style = f.read()
            self.setStyleSheet(self.style)
            self.inputFile_widget.setStyleSheet(self.style)

        self.setLabels()
        self.setLayouts()

        # 布局
    def setLabels(self):
        self.file_button1 = QPushButton("浏览...")
        self.file_button1.setObjectName('right_file_button')
        self.file_lable1 =QLabel("第一步：导入正常样本的bam文件")
        self.file_lable1.setObjectName('right_step_lable')
        self.file_path1 = QLabel("未选择文件")
        self.file_path1.setObjectName('right_file_lable')

        self.file_button2 = QPushButton("浏览...")
        self.file_button2.setObjectName('right_file_button')
        self.file_lable2 = QLabel("第二步：导入测试样本的bam文件")
        self.file_lable2.setObjectName('right_step_lable')
        self.file_path2 = QLabel("未选择文件")
        self.file_path2.setObjectName('right_file_lable')

        self.file_lable3_1 = QLabel("或导入文件：")
        self.file_lable3_1.setObjectName('right_file_lable')
        self.file_button3 = QPushButton("浏览...")
        self.file_button3.setObjectName('right_file_button')
        self.file_lable3 = QLabel("第三步：导入exon区域：输入数据")
        self.file_lable3.setObjectName('right_step_lable')
        self.file_path3 = QLabel("未选择文件")
        self.file_path3.setObjectName('right_file_lable')

        self.file_lable4_1 = QLabel("或导入文件：")
        self.file_lable4_1.setObjectName('right_file_lable')
        self.file_button4 = QPushButton("浏览...")
        self.file_button4.setObjectName('right_file_button')
        self.file_lable4 = QLabel("第四步：导入外显子的gc含量：输入数据")
        self.file_lable4.setObjectName('right_step_lable')
        self.file_path4 = QLabel("未选择文件")
        self.file_path4.setObjectName('right_file_lable')

        self.file_text3=QTextEdit()
        self.file_text3.setObjectName("right_file_text")
        self.file_text4 = QTextEdit()
        self.file_text4.setObjectName("right_file_text")

        self.pre_button=QPushButton("上一步")
        self.pre_button.setObjectName("pre_button")
        self.run_button = QPushButton("运行")
        self.run_button.setObjectName("run_button")

        self.space1 = QLabel()
        self.space2 = QLabel()
        self.space3 = QLabel()


    #定义布局
    def setLayouts(self):
        self.mainLayout = QGridLayout(self.inputFile_widget)
        self.right_fileList_layout = QGridLayout()
        self.right_fileList_widget = QWidget()
        self.right_fileList_widget.setLayout(self.right_fileList_layout)
        self.right_fileList_layout.addWidget(self.file_lable1,0,1,1,3)
        self.right_fileList_layout.addWidget(self.file_button1,1,1,1,1)
        self.right_fileList_layout.addWidget(self.file_path1, 1, 2, 1, 3)

        self.right_fileList_layout.addWidget(self.file_lable2, 3, 1, 1, 3)
        self.right_fileList_layout.addWidget(self.file_button2, 4, 1, 1, 1)
        self.right_fileList_layout.addWidget(self.file_path2, 4, 2, 1, 3)

        self.right_fileList_layout.addWidget(self.file_lable3, 6, 1, 1, 3)
        self.right_fileList_layout.addWidget(self.file_text3, 7, 1, 1, 5)
        self.right_fileList_layout.addWidget(self.file_lable3_1, 8, 1, 1, 1)
        self.right_fileList_layout.addWidget(self.file_button3, 8, 2, 1, 1)
        self.right_fileList_layout.addWidget(self.file_path3, 8, 3, 1, 3)

        self.right_fileList_layout.addWidget(self.file_lable4, 10, 1, 1, 3)
        self.right_fileList_layout.addWidget(self.file_text4, 11, 1, 1, 5)
        self.right_fileList_layout.addWidget(self.file_lable4_1, 12, 1, 1, 1)
        self.right_fileList_layout.addWidget(self.file_button4, 12, 2, 1, 1)
        self.right_fileList_layout.addWidget(self.file_path4, 12, 3, 1, 3)

        self.right_fileList_layout.addWidget(self.space1, 0, 0, 1, 1)
        self.right_fileList_layout.addWidget(self.space2, 0, 6, 1, 1)
        self.right_fileList_layout.setColumnStretch(0, 0.5)
        self.right_fileList_layout.setColumnStretch(1, 1)
        self.right_fileList_layout.setColumnStretch(2, 1)
        self.right_fileList_layout.setColumnStretch(3, 1)
        self.right_fileList_layout.setColumnStretch(4, 1.5)
        self.right_fileList_layout.setColumnStretch(5, 1.5)
        self.right_fileList_layout.setColumnStretch(6, 0.5)

        self.right_fileList_layout.setRowStretch(0, 2)
        self.right_fileList_layout.setRowStretch(1, 2)
        self.right_fileList_layout.setRowStretch(2, 1)
        self.right_fileList_layout.setRowStretch(3, 2)
        self.right_fileList_layout.setRowStretch(4, 2)
        self.right_fileList_layout.setRowStretch(5, 1)
        self.right_fileList_layout.setRowStretch(6, 2)
        self.right_fileList_layout.setRowStretch(7, 4)
        self.right_fileList_layout.setRowStretch(8, 2)
        self.right_fileList_layout.setRowStretch(9, 1)
        self.right_fileList_layout.setRowStretch(10, 2)
        self.right_fileList_layout.setRowStretch(11, 4)
        self.right_fileList_layout.setRowStretch(12, 2)
        self.right_fileList_layout.setRowStretch(13, 2)
        self.right_fileList_layout.setRowStretch(14, 4)

        self.right_fileList_layout.addWidget(self.pre_button, 14, 4, 1, 1)
        self.right_fileList_layout.addWidget(self.run_button, 14, 5, 1, 1)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.right_fileList_widget, 0, 0, 12, 9)







