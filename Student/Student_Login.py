import sys
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl, pyqtSlot, QTimer
from Export_USB import readText

class StudentLogin(QWidget):
    def __init__(self, parent=None):
        super.__init__()

        # Frame
        self.title = "Student Login"
        self.top = 50
        self.bottom = 50
        self.left = 50
        self.right = 50
        self.height = 100
        self.width = 200
        self.login = ""
        self.count = 100 #allow 100 second for each student to log in

        # Check student name, id
        # self.hash.

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        # Set Label for the UI
        self.label = QLabel(self)
        self.label.resize(1500, 70)


        # Handling the log-in error
        self.label_error = QLabel("Login Error!, \nPlease Swipe The Card Again!")
        self.label_error.setStyleSheet("color:red")
        self.label_error.resize(400,20)
        self.label_error.move(20,100)
        self.label_error.hide()

        # After Successful Student Log-in
        self.timer = QTimer()
        self.timer.timeout().connect(self.countdown)
        self.timer.start(1000) # Allow 1000 second per student


        # Alternate Log-In method (Fingerprint)
        fingerprint_login = QLabel("Fingerprint Log-In")
        fingerprint_login.move(200,480)



        student_label = QLabel("Name: ", self)


    def countdown(self):
        if self.count < 1:
            self.init_ui()

        now = datetime.datetime.now()
        self.label.setText("Time now: %s. End Time: %s. Second Left: %s" %(
            now.strftime("%H:%M:%S"), (now+datetime.timedelta(seconds=self.count)).strftime("%H:%M:%S"),self.count ))
        self.count = self.count - 1


    def open_window(self):
        if(self.name):
            print("You are Check-in")
            student.close()
        else:
            self.label_error.show()
            print("Check-in Failed, Try Alternate Log-In Method")





# Action
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    student = StudentLogin()
    student.show()
    sys.exit(app.exec_())