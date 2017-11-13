import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl, pyqtSlot
from Hashing_PBKDF2 import PBKDF2_Algorithm
from User_Interface import Admin_Login


class Reset_Password_Input(QMainWindow):
    def __init__(self, username,email,parent=None):
        super().__init__()
        self.title = 'Reset Password'
        self.left = 50
        self.top = 50
        self.width = 300
        self.height = 480
        print(username)
        self.username=username
        print(email)
        self.email=email
        self.hash=PBKDF2_Algorithm.PBKDF2_Algorithm
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label_login_error = QLabel("login error,\ncheck your credentials", self)
        self.label_login_error.setStyleSheet("color:red")
        self.label_login_error.resize(300, 80)
        self.label_login_error.move(25, 250)
        self.label_login_error.hide()

        label_logo = QLabel(self)
        pixmap_logo = QPixmap('placeholder.png')
        label_logo.setPixmap(pixmap_logo)
        label_logo.resize(200, 200)
        label_logo.move(50, 50)

        label_password = QLabel('Password:', self)
        label_password.move(25, 300)
        self.textbox_password = QLineEdit(self)
        self.textbox_password.resize(250, 20)
        self.textbox_password.move(25, 330)
        self.textbox_password.setEchoMode(QLineEdit.Password)
        self.textbox_password.returnPressed.connect(self.open_register_window)

        label_re_password = QLabel('Re-enter password:', self)
        label_re_password.move(25, 360)
        label_re_password.setMinimumWidth(300)
        self.textbox_re_password = QLineEdit(self)
        self.textbox_re_password.resize(250, 20)
        self.textbox_re_password.move(25, 390)
        self.textbox_re_password.setEchoMode(QLineEdit.Password)
        self.textbox_re_password.returnPressed.connect(self.open_register_window)

        login_button = QPushButton('Main Menu', self)
        login_button.setToolTip('Return to main menu')
        login_button.move(25, 430)
        login_button.clicked.connect(self.main_menu)

        login_button = QPushButton('Reset', self)
        login_button.setToolTip('Register an admin account')
        login_button.move(175, 430)
        login_button.clicked.connect(self.open_register_window)

    @pyqtSlot()

    def main_menu(self):
        self.close()
        self.newWindow = Admin_Login.AdminLogin()
        self.newWindow.show()

    def open_register_window(self):
            if(self.textbox_password.text() == '' or self.textbox_re_password.text() ==''):
                self.label_login_error.setText("passwords cannot be empty")
                self.label_login_error.show()
            elif(self.hash.check_Identical_Password(self,self.textbox_password.text(),self.textbox_re_password.text())):
                if(self.hash.check_Password_Length(self,self.textbox_password.text())):
                    if(self.hash.check_Special_Character(self.textbox_password.text())):
                        self.password=self.textbox_password.text()
                        self.hash.generate_Hash(object,self.username,self.password,self.email)
                        QMessageBox.question(self, 'Student Attendance Service',"Password had been reset", QMessageBox.Ok)
                        self.close()
                        self.newWindow = Admin_Login.AdminLogin()
                        self.newWindow.show()
                    else:
                        self.label_login_error.setText("Please make sure your password\nhave 1 upper 1 lower\n1 number 1 special character")
                        self.label_login_error.show()
                else:
                    self.label_login_error.setText("passwords length need\nto be between 6 to 16\ncharacters")
                    self.label_login_error.show()
            else:
                self.label_login_error.setText("passwords is not identical")
                self.label_login_error.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    reset_admin = Reset_Password_Input()
    reset_admin.show()
    sys.exit(app.exec_())
