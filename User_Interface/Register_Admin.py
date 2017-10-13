import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl, pyqtSlot
from Hashing_PBKDF2 import PBKDF2_Algorithm
from User_Interface import Admin_Login

class Register_Admin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.title = 'Administrator Register'
        self.left = 50
        self.top = 50
        self.width = 300
        self.height = 550
        self.hash=PBKDF2_Algorithm.PBKDF2_Algorithm
        self.init_ui()
        self.newWindow=Admin_Login

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

        label_name = QLabel('Username:', self)
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

        label_re_password = QLabel('Re-enter password:', self)
        label_re_password.move(25, 415)
        label_re_password.setMinimumWidth(300)
        self.textbox_re_password = QLineEdit(self)
        self.textbox_re_password.resize(250, 20)
        self.textbox_re_password.move(25, 445)
        self.textbox_re_password.setEchoMode(QLineEdit.Password)

        login_button = QPushButton('Register', self)
        login_button.setToolTip('Register an admin account')
        login_button.move(175, 480)
        login_button.clicked.connect(self.open_register_window)

    @pyqtSlot()

    def open_register_window(self):
        if self.textbox_name.text()=='':
            print("textbox is empty")
            self.label_login_error.show()
        elif(self.hash.check_Avaliable_Username(self,self.textbox_name.text())):
            print("username is avaliable")
            self.label_login_error.hide()
            if(self.hash.check_Identical_Password(self,self.textbox_password.text(),self.textbox_re_password.text())):
                if(self.hash.check_Password_Length(self,self.textbox_password.text())):
                    if(self.hash.check_Special_Character(self.textbox_password.text())):
                        # show_Exit_Dialog(self)
                        msg = QMessageBox(self)
                        msg.setIcon(QMessageBox.Question)
                        msg.setWindowTitle('Confirmation')
                        msg.setText('Register Sucess!:')
                        another_admin = msg.addButton('Register Another Admin', QMessageBox.AcceptRole)
                        return_SignIn = msg.addButton('Return to Sign-in', QMessageBox.AcceptRole)
                        quit = msg.addButton('Exit Program', QMessageBox.RejectRole)
                        msg.setDefaultButton(return_SignIn)
                        msg.exec_()
                        msg.deleteLater()

                        if msg.clickedButton() is another_admin:
                            self.restart()
                        elif msg.clickedButton() is return_SignIn:
                            self.newWindow.AdminLogin(self)
                            register_admin.close()
                        else:
                            self.close()
                    else:
                        print("Please make sure your password have 1 upper 1 lower 1 number 1 special cahracter")
                else:
                    print("passwords length need to be between 6 to 16 characters")
            else:
                print("passwords is not identical")
                self.label_login_error.show()

        else:
            print("username is taken")
            self.label_login_error.show()

    # def show_Exit_Dialog(self):
    #     msg = QMessageBox(self)
    #     msg.setIcon(QMessageBox.Question)
    #     msg.setWindowTitle('Confirmation')
    #     msg.setText('Register Sucess!:')
    #     another_admin = msg.addButton('Register Another Admin', QMessageBox.AcceptRole)
    #     return_SignIn = msg.addButton('Return to Sign-in', QMessageBox.AcceptRole)
    #     quit = msg.addButton('Exit Program', QMessageBox.RejectRole)
    #     msg.setDefaultButton(return_SignIn)
    #     msg.exec_()
    #     msg.deleteLater()
    #
    #     if msg.clickedButton() is another_admin:
    #         print('RESTART')
    #         self.restart()
    #     elif msg.clickedButton() is return_SignIn:
    #         self.newWindow.show()
    #         register_admin.close()
    #     else:
    #         self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    register_admin = Register_Admin()
    register_admin.show()
    sys.exit(app.exec_())
