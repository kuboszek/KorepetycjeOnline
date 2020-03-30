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
from PyQt5.QtWidgets import QApplication,QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsEllipseItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter

class GUI(QGraphicsView):
    def __init__(self):
        self.scene = QGraphicsScene()
        super().__init__(self.scene)

        self.scene.setSceneRect(0,0, 400, 400);
            #uic.loadUi('gui.ui', self)
        #self.setFixedSize(self.size())
        #self.set
        #rect = QGraphicsRectItem();
        #rect.setRect(-100,-100, 100, 100);
        #super().setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform);
        #rect.setBrush(Qt.darkGreen);
       # self.scene.addItem(rect);

        self.show()

    def mousePressEvent(self, e):
        print(e.pos())

        ellipse = QGraphicsEllipseItem();
        ellipse.setRect(e.pos().x()-5, e.pos().y()-5, 10, 10);
        ellipse.setBrush(Qt.darkGreen);
        self.scene.addItem(ellipse);


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec_())      