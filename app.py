import sys
import io
import os
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QBuffer, QRect, QSize, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QCursor, QPalette, QIcon
from PIL import Image
import pytesseract
from pynput.mouse import Button, Controller
import time
import pyperclip

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.start, self.end = QPoint(), QPoint()
        self.fullWindow()

    def fullWindow(self):
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Capture')
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Dialog)
        self.setWindowFlags(flags)
        self.showMaximized()
        self.setStyleSheet("background-color: rgba(255,255,255,0.0); border: 3px solid rgb(16, 229, 125);")
        self.show()

    def mousePressEvent(self, session):
        mouse = Controller()
        self.cropStart = mouse.position
        self.start = self.end = session.pos()
        self.update()
        self.screen = QApplication.screenAt(QCursor.pos()).grabWindow(0)
        self.screenShot = self.screen.copy(QRect(QPoint(0, 0), QSize(-1, -1)))
        return super().mousePressEvent(session)

    def mouseReleaseEvent(self, session):
        if self.start == self.end:
            return super().mouseReleaseEvent(session)
        mouse = Controller()
        self.cropEnd = mouse.position
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
        painter.setPen(QPen(QColor.fromRgbF(0,0,0,1.0), 1, Qt.SolidLine))
        painter.setBrush(QBrush(QColor.fromRgbF(255,255,255,0.2), Qt.SolidPattern))
        painter.drawRect(QRect(self.start, self.end))

    def openPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle('Are you sure?')
        msg.setText('Do you want to confirm selection?')
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Retry)
        msg.setDefaultButton(QMessageBox.Yes)
        self.start, self.end = QPoint(), QPoint()
        self.update()
        self.resizedImage = self.screenShot.scaled(screenWidth, screenHeight)
        self.resizedImage.save('capture.png')
        self.resizedImage = Image.open('./capture.png')
        msg.buttonClicked.connect(self.retry)
        msg.exec()

    def retry(self, i):
        if(i.text() == 'Retry'):
            os.remove('capture.png')
            pass
        else:
            selectedArea = self.resizedImage.crop((self.cropStart[0], self.cropStart[1], self.cropEnd[0], self.cropEnd[1]))
            selectedArea.save('selected.png')
            os.remove('capture.png')
            self.convertToText(selectedArea)
        
    def convertToText(self, screenShot):
        # buffer = QBuffer()
        # buffer.open(QBuffer.ReadWrite)
        # screenShot.save(buffer, "PNG")
        # img = Image.open(io.BytesIO(buffer.data()))
        # buffer.close()
        result = pytesseract.image_to_string(screenShot, timeout=10)
        pyperclip.copy(result)
        os.remove('selected.png')
        if(result == ''):
            self.displayError()
        else:
            print(f'Result coppied to clipboard')
            self.displayExit()

    def displayExit(self):
        msg = QMessageBox()
        msg.setWindowTitle('Coppied')
        msg.setText('The obtained result has been coppied to the clpiboard')
        msg.setIcon(QMessageBox.NoIcon)
        msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
        msg.setDefaultButton(QMessageBox.Close)
        msg.buttonClicked.connect(self.exit)
        msg.exec()

    def displayError(self):
        msg = QMessageBox()
        msg.setWindowTitle('Error')
        msg.setText('No text was found.')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
        msg.setDefaultButton(QMessageBox.Retry)
        msg.buttonClicked.connect(self.exit)
        msg.exec()

    def exit(self, i):
        if(i.text() == 'Retry'):
            pass
        else:
            QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screenWidth = app.primaryScreen().size().width()
    screenHeight = app.primaryScreen().size().height()
    window = Window()
    sys.exit(app.exec())