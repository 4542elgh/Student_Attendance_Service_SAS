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
from fingerprintScannerPy3 import settings, fps
import csv


class FingerprintSetup(QWidget):
    def __init__(self, student, students, file_name, file_extension):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.left = 200
        self.top = 200
        self.width = 665
        self.height = 200

        self.students = students
        self.student = student
        self.file_name = file_name
        self.file_extension = file_extension
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

        index = -1
        count = 0

        if self.student.getFingerprintIndex() == "-1":
            index = self.fp_enrollment(f)

            print("Your fingerprint was registered successfully and you have been marked present!")

            self.student.setFingerprintIndex(index)
            self.student.setAttendance("Present")
            self.close()
        else:
            self.fp_identify(f, self.student.getFingerprintIndex())

        self.save_roster()
        self.close()

    def fp_enrollment(self, f):
        print("Wait for the blue light to appear on the fingerprint scanner!")
        if f.init():
            f.open()
            for i in range(10):
                index = f.enroll()
                print("Enroll: " + str(index))
                f.close()
                return index

        return -1

    def fp_identify(self, f, fp_id):
        if f.init():
            f.open()

            print("Wait for the blue light to appear on the fingerprint scanner!")

            for i in range(10):

                index = f.identify()

                if index == int(fp_id):
                    print("Fingerprint Matched!")
                    self.student.setAttendance("Present")
                    time.sleep(1)
                    f.close()
                    self.close()
                else:
                    print("no match")

                time.sleep(1)

            f.close()

    def save_roster(self):
        if self.file_extension == "csv":
            Export_File.exportCSV.exportToFile(object,self.file_name,self.students)
        elif self.file_extension == "xml":
            Export_File.exportXML.exportToFile(object,self.file_name,self.students)
        else:
            Export_File.exportJSON.exportToFile(object,self.file_name,self.students)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FingerprintSetup()
    sys.exit(app.exec_())