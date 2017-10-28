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
        self.count = 15
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label = QLabel(self)
        self.label.resize(1200, 40)
        #self.interval = 1500
        self.timer = QTimer()
        print("working")
        self.timer.timeout.connect(self.countdown)
        print("working 2")
        self.timer.start(1000)

    def countdown(self):
        print("working 3")
        print("works?")
        if self.count < 1:
            self.count = 15
        print("datetime work?")
        now = datetime.datetime.now()
        print("working?")
        self.label.setText('Time now: %s. End time: %s. Seconds left: %s' % (
            now.strftime("%H:%M:%S"), (now + datetime.timedelta(seconds=self.count)).strftime("%H:%M:%S"), self.count))
        self.count = self.count - 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = StudentLogin()
    admin.show()
    sys.exit(app.exec_())