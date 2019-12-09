import math
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import QRect, Qt, QPoint, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
import cv2
import sys

chrLength=[248956422,242193529,198295559,190214555,181538259,170805979,159345973,145138636, 138394717,
           133797422,135086622,133275309,114364328,107043718,101991189,90338345,83257441,80373285,
           58617616,64444167,46709983,50818468,156040895,57227415]

class MyLabel(QLabel):
    x0 = 0
    x1 = 0
    flag = False
    chrNum=0
    goSignal = pyqtSignal(list)


    #鼠标点击事件
    def mousePressEvent(self,event):
        self.flag = True
        self.x0 = event.x()
        # print(self.mapToGlobal(QPoint(0,0)))

    #鼠标释放事件
    def mouseReleaseEvent(self,event):
        self.flag = False
        self.start = int(chrLength[self.chrNum] * self.x0 / 580)
        self.end = math.ceil(chrLength[self.chrNum] * self.x1 / 580)
        if self.start > self.end:
            temp = self.start
            self.start = self.end
            self.end = temp
        self.goSignal.emit([self.chrNum,self.start,self.end])






    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.flag:
            self.x1 = event.x()
            self.update()

    # go按钮被按下
    def goButtonEvent(self):
        self.update()

    # 绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)
        rect = QRect(self.x0, 2, abs(self.x1 - self.x0), 23)
        # rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.drawRect(rect)




