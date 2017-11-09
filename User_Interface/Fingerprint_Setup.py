import os
import sys
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton,QHBoxLayout,QMessageBox,QLabel
from PyQt5.QtCore import pyqtSlot,QEvent
from PyQt5 import QtCore
from Import_Export import Import_File,Export_File
from Add_Edit_Delete import ModifyEntry
from Student import Student
from User_Interface import Add_Student
from fpspy3 import settings, fps
import csv


class FingerprintSetup(QWidget):
    def __init__(self, student):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.left = 200
        self.top = 200
        self.width = 665
        self.height = 200

        self.student = student

        self.init_ui()

    def init_ui(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle("Fingerprint Registration")
        self.show()
        self.register_fp()

    def register_fp(self):
        f = fps.Fingerprint(settings.PORT_FINGERPRINTSCANNER, 115200)

        def signal_handler(signum, frame):
            f.close_serial()

        fps.signal.signal(fps.signal.SIGINT, signal_handler)

        if self.student.get_fingerprint_id() == -1:
            index = -1
            attempts = 0

            while index == -1 and attempts < 3:
                index = self.fp_enrollment(f)
                attempts += 1

            print("Your fingerprint was registered successfully and you have been marked present!")

            self.student.set_fingerprint_id(index)
            self.student.setAttendance("Present")

        else:
            self.fp_identify(f, self.student.get_fingerprint_id())


    def fp_enrollment(self, f):
        print("Wait for the blue light to appear on the fingerprint scanner!")
        if f.init():
            f.open()
            index = f.enroll()
            print("Enroll: " + str(index))
            f.close()
            return index

        return -1

    def fp_identify(self, f, fp_id):
        if f.init():
            f.open()

            print("Wait for the blue light to appear on the fingerprint scanner!")
            index = f.identify()

            f.close()

        if index == fp_id:
            print("Fingerprint Matched!")
            self.student.setAttendance("Present")

        else:
            print("No match!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FingerprintSetup()
    sys.exit(app.exec_())