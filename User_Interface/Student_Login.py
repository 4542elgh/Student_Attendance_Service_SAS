import sys
import datetime
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import QTimer


class StudentLogin(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.title = 'Student Login'
        self.left = 50
        self.top = 50
        self.width = 1200
        self.height = 515
        self.count = 100
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel(self)
        self.label.resize(1200, 40)

        #self.interval = 1500
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = StudentLogin()
    admin.show()
    sys.exit(app.exec_())