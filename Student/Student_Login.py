import sys
import threading
import datetime
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QProgressBar, QStyleFactory,QMessageBox
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
from User_Interface import Attendance_For_The_Day, Fingerprint_Setup, Custom_Message_Box


class StudentLogin(QWidget):
    def __init__(self, startTime, endTime, file_path, file_extension, studentList, parent=None):
        super().__init__()
        print(len(studentList))
        self.title = 'Student Login'
        self.left = 50
        self.top = 50
        self.width = 1200
        self.height = 515
        self.count = endTime
        self.startTime=startTime

        self.file_path=file_path
        self.file_extension = file_extension
        self.studentList=studentList
        self.student = None

        for student in self.studentList:
            print(student.getCIN())

        self.login = ""
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        font = QFont()
        font.setFamily("FreeMono")
        font.setPointSize(24)

        self.label = QLabel(self)
        self.label.resize(1200, 40)
        self.label.move(100, 75)
        self.label.setFont(font)

        swipe_font = QFont()
        swipe_font.setFamily("FreeMono")
        swipe_font.setPointSize(14)

        swipe_label = QLabel("Please swipe your Student ID:", self)
        swipe_label.setStyleSheet("color: rgb(255, 0, 0)")
        swipe_label.setFont(swipe_font)
        swipe_label.move(100, 355)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(100, 380, 1050, 30)

        self.timer = QTimer()
        self.timer.timeout.connect(self.count_down_to_Start)
        self.timer.start(1000)

    def count_down_to_Start(self):
        if self.startTime < 1:
            self.init_count_end()
        now = datetime.datetime.now()

        self.label.setText('Time now: %s. End time: %s. Time Until Start: %02d:%02d:%02d' % (now.strftime("%H:%M:%S"), (now + datetime.timedelta(seconds=self.startTime)).strftime("%H:%M:%S"), (self.startTime//3600)%24,(self.startTime//60)%60,self.startTime%60))
        self.startTime = self.startTime - 1

    def init_count_end(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.count_down_to_End)
        self.timer.start(1000)

    def count_down_to_End(self):
        if self.count < 1:
            QMessageBox.question(self, 'Student Attendance Service',"Attendance for xxx class has ended", QMessageBox.Ok)
            self.summary=Attendance_For_The_Day.Attendance_For_The_Day(self.file_path,self.studentList)
            self.summary.show()
            self.close()
            self.timer.stop()
        now = datetime.datetime.now()
        self.label.setText('Time now: %s. End time: %s. Time left: %02d:%02d:%02d' % (now.strftime("%H:%M:%S"), (now + datetime.timedelta(seconds=self.count)).strftime("%H:%M:%S"), (self.count//3600)%24,(self.count//60)%60,self.count%60))
        self.count = self.count - 1

    def keyPressEvent(self, event):
        self.login = self.login + str(event.text())

        if event.key() == Qt.Key_Return:
            flc = self.decode(self.login)
            print(self.login)
            if flc[2] != "000000000":
                cin = self.enrolled(flc[2])
                self.enrolled(cin)
                Custom_Message_Box.CustomMessageBox.showWithTimeout(3, "GET READY: Wait for the blue light!",
                                                                    "Fingerprint Preparation:",
                                                                    icon=QMessageBox.Information)
                self.check_fp()
                self.progress.setValue(0)
            else:
                Custom_Message_Box.CustomMessageBox.showWithTimeout(1, "ERROR: Reswipe ID",
                                                                    "Rejected:",
                                                                    icon=QMessageBox.Information)
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

    def enrolled(self, cin):
        for i in range(0, len(self.studentList)):
            if self.studentList[i].getCIN() == cin:
                self.student = self.studentList[i]

    def open_fp_view(self):
        self.fp_view = Fingerprint_view.Fingerprint_View(self)
        self.fp_view.show()

    def check_fp(self):
        self.fp_setup = Fingerprint_Setup.FingerprintSetup(self.student, self.studentList, self.file_path,
                                                               self.file_extension)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = StudentLogin()
    admin.show()
    sys.exit(app.exec_())