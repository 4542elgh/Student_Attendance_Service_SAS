
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl, pyqtSlot
from Hashing_PBKDF2 import PBKDF2_Algorithm
from Student import Student_Login
from Export_USB import readText


class Register_Student(QMainWindow):
    def __init__(self,parent=None):
        super.__init__()
        self.title = "Student Registration"
        self.left = 50
        self.top = 50
        self.width = 200
        self.height = 500
        self.hash = PBKDF2_Algorithm.PBKDF2_Algorithm

        self.init.ui()
        #self.studentWindow = Student_Window

        self.cardSwipe = readText


    def _init_ui(self):
        self.setWindowTitle(self.title)
        self.geometry(self.left, self.top,self.width,self.height)

    @pyqtSlot()

    def open_register_window(self):


# Action
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    student = Register_Student()
    student.show()
    sys.exit(app.exec_())

