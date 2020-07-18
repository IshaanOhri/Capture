import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor

class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        # screen = self.primaryScreen()
        
        
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
        if self.start == self.end:
            return super().mouseReleaseEvent(session)
        self.end = session.pos()
        self.update()
        self.openPopup()
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

    def openPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle('Are you sure?')
        msg.setText('Do you want to confirm selection?')
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Retry)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.buttonClicked.connect(self.retry)
        # popup = QDialog()
        # screenWidth = self.size().width()
        # screenHeight = self.size().height()
        # centerX = screenWidth / 2
        # centerY = screenHeight / 2
        # height = 100
        # width = 400
        # msg.setGeometry(int(centerX - width / 2),int(centerY - height/2),int(width),int(height))
        # popup.setModal(True)
        # popup.exec()
        msg.exec()

    def retry(self, i):
        if(i.text() == 'Retry'):
            self.start, self.end = QtCore.QPoint(), QtCore.QPoint()
        else:
            print(i.text())
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())