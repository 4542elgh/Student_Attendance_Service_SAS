import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton,QMessageBox
from PyQt5.QtGui import QIcon, QPixmap,QRegExpValidator
from PyQt5.QtCore import QUrl, pyqtSlot,QRegExp
from PyQt5 import QtCore
from User_Interface import Load_Roster
# from User_Interface import Register_Admin
from User_Interface import Reset_Password
from Hashing_PBKDF2 import PBKDF2_Algorithm
from User_Interface import Display_Roster
from Student import Student


class Add_Student(QMainWindow):
    def __init__(self, display_roster, parent=None):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.title = 'Administrator Login'
        self.left = 50
        self.top = 50
        self.width = 300
        self.height = 250
        self.display_roster = display_roster
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width,self.height)

        self.label_login_error = QLabel("", self)
        self.label_login_error.setStyleSheet("color:red")
        self.label_login_error.resize(300, 80)
        self.label_login_error.move(25, 0)
        self.label_login_error.hide()

        firstNameLabel = QLabel('First Name:', self)
        firstNameLabel.move(25, 50)
        self.firstNameBox = QLineEdit(self)
        self.firstNameBox.resize(250, 20)
        self.firstNameBox.move(25, 75)
        self.firstNameBox.returnPressed.connect(self.add)

        lastNameLabel = QLabel('Last Name:', self)
        lastNameLabel.move(25, 100)
        self.lastNameBox = QLineEdit(self)
        self.lastNameBox.resize(250, 20)
        self.lastNameBox.move(25, 125)
        self.lastNameBox.returnPressed.connect(self.add)

        CINLabel = QLabel('CIN:', self)
        CINLabel.move(25, 150)
        self.CINBox = QLineEdit(self)
        self.CINBox.resize(250, 20)
        self.CINBox.move(25, 175)
        self.CINBox.returnPressed.connect(self.add)
        reg_ex = QRegExp("^[0-9]{9}$")
        input_validator = QRegExpValidator(reg_ex, self.CINBox)
        self.CINBox.setValidator(input_validator)

        self.add_button = QPushButton("Add",self)
        self.add_button.resize(120,30)
        self.add_button.move(25,205)
        self.add_button.clicked.connect(self.add)

        self.discard_button = QPushButton("Discard", self)
        self.discard_button.resize(120, 30)
        self.discard_button.move(155, 205)
        self.discard_button.clicked.connect(self.discard)

    @pyqtSlot()
    def add(self):
        if self.firstNameBox.text()=='' or self.lastNameBox.text()=='' or self.CINBox.text()=='':
            self.label_login_error.setText("Fields cannot be empty")
            self.label_login_error.show()
        else:
            self.display_roster.append_student(Student.Student(self.firstNameBox.text(), self.lastNameBox.text(), self.CINBox.text()))
            self.close()

    def discard(self):
        QMessageBox.question(self, 'Student Attendance Service', "Changes has been discarded", QMessageBox.Ok)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = Add_Student()
    admin.show()
    sys.exit(app.exec_())