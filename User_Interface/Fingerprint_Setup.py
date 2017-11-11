import os
import sys
import time
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton,QHBoxLayout,QMessageBox,QLabel
from PyQt5.QtCore import pyqtSlot,QEvent
from PyQt5 import QtCore
from Import_Export import Import_File,Export_File
from Add_Edit_Delete import ModifyEntry
from Student import Student
from User_Interface import Custom_Message_Box
from fingerprintScannerPy3 import settings, fps
import csv


class FingerprintSetup:
    def __init__(self, student, students, file_name, file_extension):
        self.students = students
        self.student = student
        self.file_name = file_name
        self.file_extension = file_extension

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

            if index == -1:
                Custom_Message_Box.CustomMessageBox.showWithTimeout(2, "UNRECOGNIZED: No print registered!",
                                                                    "Rejected:",
                                                                    icon=QMessageBox.Warning)
            else:
                self.student.setFingerprintIndex(index)
                self.student.setAttendance("Present")
                Custom_Message_Box.CustomMessageBox.showWithTimeout(2, "ACCEPTED: Your fingerprint was registered!",
                                                                    "Success:",
                                                                    icon=QMessageBox.Information)
        else:
            self.fp_identify(f, self.student.getFingerprintIndex())

        self.save_roster()

    def fp_enrollment(self, f):
        if f.init():
            f.open()
            for i in range(1):
                index = f.enroll()
                f.close()
                return index

        return -1

    def fp_identify(self, f, fp_id):

        if f.init():
            f.open()

            for i in range(2):

                index = f.identify()

                if index == int(fp_id):

                    self.student.setAttendance("Present")
                    time.sleep(1)
                    Custom_Message_Box.CustomMessageBox.showWithTimeout(1, "SUCCESS!",
                                                                        "Accepted:",
                                                                        icon=QMessageBox.Information)
                    break
                else:
                    Custom_Message_Box.CustomMessageBox.showWithTimeout(1, "UNRECOGNIZED: Reposition print!",
                                                                        "Rejected:",
                                                                        icon=QMessageBox.Warning)
                # if i == 1:
                #     Custom_Message_Box.CustomMessageBox.showWithTimeout(2, "ERROR: PLEASE SEE YOUR ADMINISTRATOR!",
                #                                                         "ERROR:",
                #                                                         icon=QMessageBox.Critical)

                time.sleep(1)

            f.close()

    def save_roster(self):
        if self.file_extension == "csv":
            Export_File.exportCSV.exportToFile(object,self.file_name,self.students)
        elif self.file_extension == "xml":
            Export_File.exportXML.exportToFile(object,self.file_name,self.students)
        else:
            Export_File.exportJSON.exportToFile(object,self.file_name,self.students)