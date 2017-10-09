import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl, pyqtSlot
from Load_Roster import LoadRoster
from Hashing_PBKDF2 import PBKDF2_Algorithm

class AdminLogin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.title = 'Administrator Login'

        self.left = 50
        self.top = 50
        self.width = 300
        self.height = 480
        self.hash=PBKDF2_Algorithm.PBKDF2_Algorithm
        self.hash.generate_Hash(self,'admin','000000')
        self.init_ui()

        self.newWindow = LoadRoster(self)

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

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

        alternate_login = QLabel('Alternate Login', self)
        alternate_login.setText('''<a href='smileman.gif'>Alternate Login</a>''')
        alternate_login.setOpenExternalLinks(True)
        alternate_login.move(200, 450)

        self.show()

    @pyqtSlot()
    def open_window(self):
        print(self.hash.check_Password(self,self.textbox_name.text(),self.textbox_password.text()))
        admin.close()
        self.newWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = AdminLogin()
    sys.exit(app.exec_())
