import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.start, self.end = QtCore.QPoint(), QtCore.QPoint()
        self.fullWindow()

    def fullWindow(self):
        self.setWindowTitle('Capture')
        flags = QtCore.Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Dialog)
        self.setWindowFlags(flags)
        self.showMaximized()
        self.setStyleSheet("background-color: rgba(255,255,255,0.0); border: 3px solid rgb(16, 229, 125);")
        self.show()

    def mousePressEvent(self, session):
        self.start = self.end = session.pos()
        self.update()
        return super().mousePressEvent(session)

    def mouseReleaseEvent(self, session):
        self.end = session.pos()
        self.update()
        return super().mouseReleaseEvent(session)

    def mouseMoveEvent(self, session):
        self.end = session.pos()
        self.update()
        return super().mousePressEvent(session)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.white, 1, Qt.SolidLine))
        painter.setBrush(QBrush(QColor.fromRgbF(255,255,255,0.2), Qt.SolidPattern))
        painter.drawRect(QtCore.QRect(self.start, self.end))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())