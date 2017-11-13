import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton,QShortcut
from PyQt5.QtGui import QIcon, QPixmap,QKeySequence,QImage
from PyQt5.QtCore import QUrl, pyqtSlot
from User_Interface import Load_Roster
from User_Interface import Register_Admin
from User_Interface import Reset_Password
from Hashing_PBKDF2 import PBKDF2_Algorithm
from User_Interface import Attendance_For_The_Day
from Student import Student


class AdminLogin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.title = 'Administrator Login'
        self.left = 50
        self.top = 50
        self.width = 300
        self.height = 515
        self.hash=PBKDF2_Algorithm.PBKDF2_Algorithm
        self.hash.generate_Hash(self,'admin','000000','admin@example.com')
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width,self.height)

        self.label_login_error = QLabel("login error,\ncheck your credentials", self)
        self.label_login_error.setStyleSheet("color:red")
        self.label_login_error.resize(300,40)
        self.label_login_error.move(25, 265)
        self.label_login_error.hide()

        label_logo = QLabel(self)
        pixmap_logo = QPixmap('logo.png')
        label_logo.setPixmap(pixmap_logo)
        label_logo.resize(200, 200)
        label_logo.move(50, 60)

        image = QImage();
        image.load("logo.png");
        image.save("logo2.png");

        label_name = QLabel('Name:', self)
        label_name.move(25, 300)
        self.textbox_name = QLineEdit(self)
        self.textbox_name.resize(250, 20)
        self.textbox_name.move(25, 330)
        self.textbox_name.returnPressed.connect(self.open_window)

        label_password = QLabel('Password:', self)
        label_password.move(25, 355)
        self.textbox_password = QLineEdit(self)
        self.textbox_password.resize(250, 20)
        self.textbox_password.move(25, 385)
        self.textbox_password.setEchoMode(QLineEdit.Password)
        self.textbox_password.returnPressed.connect(self.open_window)

        login_button = QPushButton('Login', self)
        login_button.setToolTip('Login')
        login_button.move(175, 420)
        login_button.clicked.connect(self.open_window)

        register_button = QPushButton('Register', self)
        register_button.setToolTip('Register an admin account')
        register_button.move(25, 420)
        register_button.clicked.connect(self.open_register_admin_window)

        reset_button = QPushButton('Reset', self)
        reset_button.setToolTip('Reset Admin Password')
        reset_button.move(25, 460)
        reset_button.clicked.connect(self.open_reset_password_window)

        self.shortcut = QShortcut(QKeySequence("Enter"), self)
        self.shortcut.activated.connect(self.open_window)
    @pyqtSlot()
    def open_window(self):
        if (self.hash.check_Password(self,self.textbox_name.text(),self.textbox_password.text())):
            print("Login Successful")
            self.close()
            self.newWindow = Load_Roster.LoadRoster(self)
            self.newWindow.show()
        else:
            self.label_login_error.show()
            print("Login Failed")

    def open_register_admin_window(self):
        self.close()
        self.registerWindow = Register_Admin.Register_Admin(self)
        self.registerWindow.show()

    def open_reset_password_window(self):
        self.close()
        self.resetWindow = Reset_Password.Reset_Password(self)
        self.resetWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = AdminLogin()
    admin.show()
    sys.exit(app.exec_())
