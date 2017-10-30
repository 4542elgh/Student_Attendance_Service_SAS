import sys
import datetime
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QProgressBar, QStyleFactory
from PyQt5.QtCore import QTimer, Qt


class StudentLogin(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.title = 'Student Login'
        self.left = 50
        self.top = 50
        self.width = 1200
        self.height = 515
        self.count = 100
        self.login = ""
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel(self)
        self.label.resize(1200, 40)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(100, 390, 1050, 30)

        self.timer = QTimer()
        self.timer.timeout.connect(self.countdown)
        self.timer.start(1000)

    def countdown(self):
        if self.count < 1:
            self.count = 100
        now = datetime.datetime.now()
        self.label.setText('Time now: %s. End time: %s. Seconds left: %s' % (
            now.strftime("%H:%M:%S"), (now + datetime.timedelta(seconds=self.count)).strftime("%H:%M:%S"), self.count))
        self.count = self.count - 1

    def keyPressEvent(self, event):
        self.login = self.login + str(event.text())

        if event.key() == Qt.Key_Return:
            print(self.login)
            flc = self.decode(self.login)
            print(flc)
            self.login = ""

    def decode(self, user_id):
        try:
            split = user_id.split('^')

            name = split[1]
            forward_slash = split[1].find('/')
            first_name = name[forward_slash + 1:len(name)]
            last_name = name[0:forward_slash]

            three = split[2]
            cin = three[len(three) - 11:len(three) - 2]

            self.load_bar()

            return first_name, last_name, cin
        except IndexError:
            print("Error!")

    def load_bar(self):
        self.complete = 0

        while self.complete < 100:
            self.complete += 0.0001
            self.progress.setValue(self.complete)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = StudentLogin()
    admin.show()
    sys.exit(app.exec_())