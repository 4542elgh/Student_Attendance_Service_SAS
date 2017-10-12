import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl, pyqtSlot
from Load_Roster import LoadRoster
from Register_Admin import Register_Admin
from Hashing_PBKDF2 import PBKDF2_Algorithm

class AdminLogin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.title = 'Administrator Login'

        self.left = 50
        self.top = 50
        self.width = 300
        self.height = 500
        self.hash=PBKDF2_Algorithm.PBKDF2_Algorithm
        self.hash.generate_Hash(self,'admin','000000')
        self.init_ui()

        self.newWindow=LoadRoster(self)
        self.registerWindow=Register_Admin(self)

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label_login_error = QLabel("login error,\ncheck your credentials", self)
        self.label_login_error.setStyleSheet("color:red")
        self.label_login_error.resize(300,40)
        self.label_login_error.move(40, 415)
        self.label_login_error.hide()

        label_logo = QLabel(self)
        pixmap_logo = QPixmap('placeholder.png')
        label_logo.setPixmap(pixmap_logo)
        label_logo.resize(200, 200)
        label_logo.move(50, 50)

        label_name = QLabel('Name:', self)
        label_name.move(25, 300)
        self.textbox_name = QLineEdit(self)
        self.textbox_name.resize(250, 20)
        self.textbox_name.move(25, 330)

        label_password = QLabel('Password:', self)
        label_password.move(25, 355)
        self.textbox_password = QLineEdit(self)
        self.textbox_password.resize(250, 20)
        self.textbox_password.move(25, 385)
        self.textbox_password.setEchoMode(QLineEdit.Password)

        login_button = QPushButton('Login', self)
        login_button.setToolTip('Login')
        login_button.move(175, 420)
        login_button.clicked.connect(self.open_window)

        register_button = QPushButton('Register', self)
        register_button.setToolTip('Register an admin account')
        register_button.move(25, 420)
        register_button.clicked.connect(self.open_register_admin_window)

        reset_button = QPushButton('Reset', self)
        reset_button.setToolTip('Login')
        reset_button.move(25, 460)
        reset_button.clicked.connect(self.open_window)

        alternate_login = QLabel('Alternate Login', self)
        alternate_login.setText('''<a href='smileman.gif'>Alternate Login</a>''')
        alternate_login.setOpenExternalLinks(True)
        alternate_login.move(200, 480)

        self.show()

    @pyqtSlot()
    def open_window(self):
        if (self.hash.check_Password(self,self.textbox_name.text(),self.textbox_password.text())):
            print("Login Sucessful")
            admin.close()
            self.newWindow.show()
        else:
            self.label_login_error.show()
            print("Login Failed")

    def open_register_admin_window(self):
        print("popup")
        admin.close()
        self.registerWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = AdminLogin()
    sys.exit(app.exec_())
