import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.FullWindow()

    
    def FullWindow(self):
        flags = QtCore.Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Dialog)
        self.setWindowFlags(flags)
        self.showMaximized()
        self.setStyleSheet("background-color: rgba(255,255,255,0.2); border: 3px solid rgb(16, 229, 125);")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())