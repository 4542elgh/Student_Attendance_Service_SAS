
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl, pyqtSlot
from Hashing_PBKDF2 import PBKDF2_Algorithm
from Student import Student_Login


class Register_Student(QMainWindow):
    def __init__(self,parent=None):
        super.__init__()
        self.title = "Student Registration"
        self.left = 50
        self.top = 50
        self.width = 200
        self.height = 500




