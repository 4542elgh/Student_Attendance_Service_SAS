import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Administrator Login'
        self.left = 50
        self.top = 50
        self.width = 300
        self.height = 475
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label_logo = QLabel(self)
        pixmap_logo = QPixmap('placeholder.png')
        label_logo.setPixmap(pixmap_logo)
        label_logo.resize(200, 200)
        label_logo.move(50, 50)

        label_name = QLabel('Name:', self)
        label_name.move(25, 300)
        textbox_name = QLineEdit(self)
        textbox_name.resize(250, 20)
        textbox_name.move(25, 330)

        label_password = QLabel('Password:', self)
        label_password.move(25, 355)
        textbox_password = QLineEdit(self)
        textbox_password.resize(250, 20)
        textbox_password.move(25, 385)

        alternate_login = QLabel('Alternate Login', self)
        alternate_login.setText('''<a href='smileman.gif'>Alternate Login</a>''')
        alternate_login.setOpenExternalLinks(True)
        alternate_login.move(200, 420)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())