import sys
import datetime
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QProgressBar, QStyleFactory,QMessageBox
from PyQt5.QtCore import QTimer, Qt
from User_Interface import Attendance_For_The_Day, Fingerprint_Setup


class StudentLogin(QWidget):
    def __init__(self ,startTime,endTime,file_path,studentList,parent=None):
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
        self.studentList=studentList

        for student in self.studentList:
            print(student.getCIN())

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
            print(self.login)
            flc = self.decode(self.login)
            print(flc)
            student = self.enrolled(flc[2])
            self.check_fp(student)
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
                return self.studentList[i]
        print("Student not enrolled!")

    def check_fp(self, student):
        if student.get_fingerprint_id() == -1:
            self.fp_setup = Fingerprint_Setup.FingerprintSetup(student)
            self.fp_setup.show()
        else:
            print()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = StudentLogin()
    admin.show()
    sys.exit(app.exec_())