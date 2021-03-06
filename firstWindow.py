# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsEllipseItem
# from PyQt5.QtCore import Qt
# import sys
#
# #from pynput.mouse import Button, Controller
#
# def main():
#     app = QApplication(sys.argv)
#
#     scene = QGraphicsScene()
#     view = QGraphicsView(scene)
#
#     rect = QGraphicsRectItem();
#     rect.setRect(0, 0, 600, 300);
#     rect.setBrush(Qt.darkGreen);
#     scene.addItem(rect);
#
#     #obsluga myszy
#     mouse = Controller()
#
#
#
#
#
#
#
#     view.show()
#     sys.exit(app.exec_())
#
#
# main()
import sys
#from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QApplication,  QGraphicsScene, QGraphicsLineItem, QGraphicsView, QGraphicsRectItem, QGraphicsEllipseItem
from PyQt5.QtCore import Qt, QLineF
from PyQt5.QtGui import QPainter, QPen

class GUI(QGraphicsView):
    def __init__(self):
        self.newPoint = None
        self.newPoint

        self.bgcolor = Qt.white
        self.color = 0
        self.size = 4
        self.maxSize = 10
        self.maxColors = 6
        self.colors = (Qt.black, Qt.yellow, Qt.blue, Qt.green, Qt.red, Qt.gray)
        self.scene = QGraphicsScene()
        super().__init__(self.scene)
        super().setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform);

        self.scene.setSceneRect(0,0, 1100, 700);
        self.show()

    def mouseReleaseEvent(self, QMouseEvent):
        print("release")

    def point_color(self, x, y, color, addSize):
        #print(color)

        ellipse = QGraphicsEllipseItem()
        ellipse.setRect(x - (self.size+addSize) // 2, y - (self.size+addSize) // 2, self.size +addSize, self.size+addSize)
        ellipse.setBrush(color)
        ellipse.setPen(QPen(color, self.size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        self.scene.addItem(ellipse)

    def point(self, x, y):
        self.point_color(x,y,self.colors[self.color],0)

    def del_point(self, x, y):
        self.point_color(x, y, self.bgcolor, 2)

    def mousePressEvent(self, e):
        print(e.pos())
        self.oldPoint = e.pos()
        self.newPoint = e.pos()
        self.point(e.pos().x(), e.pos().y())
        self.firstMove = True

    def mouseMoveEvent(self, e):

        self.oldPoint = self.newPoint
        self.newPoint = e.pos()
        if self.firstMove:
            #zamaz kropke
            self.del_point(self.oldPoint.x(), self.oldPoint.y())


        self.firstMove = False
        #print(self.oldPoint.x(), self.oldPoint.y(), self.newPoint.x(), self.newPoint.y())
        line = QGraphicsLineItem()

        line.setLine(QLineF(self.oldPoint.x(), self.oldPoint.y(), self.newPoint.x(),self.newPoint.y()))
        line.setPen(QPen(self.colors[self.color], self.size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        self.scene.addItem(line)


    def keyPressEvent(self, e):
        #zmiana kolorow W - nastepny , Q - poprzedni
        if e.key() == Qt.Key_W:
            self.color = (self.color + 1) % self.maxColors
            print("Zmiana koloru na ", self.color)
        elif e.key() == Qt.Key_Q:
            self.color = (self.color - 1) % self.maxColors
            print("Zmiana koloru na ", self.color)

        # zmiana kolorow S - nastepny , A - poprzedni
        elif e.key() == Qt.Key_S:
            self.size = (self.size + 1) % self.maxSize
            print("Zmiana rozmiaru na ", self.size)
        elif e.key() == Qt.Key_A:
            self.size = (self.size - 1) % self.maxSize
            print("Zmiana rozmiaru na ", self.size)
        #clear
        elif e.key() == Qt.Key_C:
            self.scene.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec_())