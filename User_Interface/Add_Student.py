import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl, pyqtSlot
from User_Interface import Load_Roster
from User_Interface import Register_Admin
from User_Interface import Reset_Password
from Hashing_PBKDF2 import PBKDF2_Algorithm


class AdminLogin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.title = 'Administrator Login'
        self.left = 50
        self.top = 50
        self.width = 300
        self.height = 250
        self.hash=PBKDF2_Algorithm.PBKDF2_Algorithm
        self.hash.generate_Hash(self,'admin','000000')
        self.init_ui()

    def init_ui(self):
        print("print init here")
        self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width,self.height)

        label_name = QLabel('Name:', self)
        label_name.move(25, 130)
        self.textbox_name = QLineEdit(self)
        self.textbox_name.resize(250, 20)
        self.textbox_name.move(25, 150)

        label_name = QLabel('Name:', self)
        label_name.move(25, 130)
        self.textbox_name = QLineEdit(self)
        self.textbox_name.resize(250, 20)
        self.textbox_name.move(25, 150)

        label_name = QLabel('Name:', self)
        label_name.move(25, 130)
        self.textbox_name = QLineEdit(self)
        self.textbox_name.resize(250, 20)
        self.textbox_name.move(25, 150)

        label_name = QLabel('Name:', self)
        label_name.move(25, 130)
        self.textbox_name = QLineEdit(self)
        self.textbox_name.resize(250, 20)
        self.textbox_name.move(25, 150)

    @pyqtSlot()
    def open_window(self):
        if (self.hash.check_Password(self,self.textbox_name.text(),self.textbox_password.text())):
            print("Login Successful")
            admin.close()
            self.newWindow = Load_Roster.LoadRoster(self)
            self.newWindow.show()
        else:
            self.label_login_error.show()
            print("Login Failed")

    def open_register_admin_window(self):
        admin.close()
        self.registerWindow = Register_Admin.Register_Admin(self)
        self.registerWindow.show()

    def open_reset_password_window(self):
        admin.close()
        self.resetWindow = Reset_Password.Reset_Password(self)
        self.resetWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = AdminLogin()
    admin.show()
    sys.exit(app.exec_())
