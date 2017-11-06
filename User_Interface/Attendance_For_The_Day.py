import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton,QHBoxLayout,QMessageBox,QLabel
from PyQt5.QtCore import pyqtSlot,QEvent
from PyQt5 import QtCore
from Import_Export import Import_File,Export_File
from Add_Edit_Delete import ModifyEntry
from Student import Student
from User_Interface import Add_Student
import time

class Attendance_For_The_Day(QWidget):
    def __init__(self, file_path,studentList):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.left = 200
        self.top = 200
        self.width = 665
        self.height = 200

        self.file_path=file_path

        self.studentList=studentList
        # self.studentList = [Student.Student("1111","ming","liu","302102","onTime")]
        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.get_summary()

        self.labelMessage = QLabel("Attendance Finished!", self)
        self.labelMessage.move(50,20)
        self.labelMessage = QLabel("On Time :", self)
        self.labelMessage.move(50, 50)
        self.labelMessage.resize(50,20)
        self.labelMessage = QLabel(str(self.onTime), self)
        self.labelMessage.move(100, 50)
        self.labelMessage.resize(50, 20)
        self.labelMessage.setStyleSheet("color:green")
        self.labelMessage = QLabel("Late :", self)
        self.labelMessage.move(50, 70)
        self.labelMessage.resize(50, 20)
        self.labelMessage = QLabel(str(self.late), self)
        self.labelMessage.move(100, 70)
        self.labelMessage.resize(50, 20)
        self.labelMessage.setStyleSheet("color:orange")
        self.labelMessage = QLabel("Absent :", self)
        self.labelMessage.move(50, 90)
        self.labelMessage.resize(50, 20)
        print(time.localtime()[0])
        print(time.localtime()[1])
        print(time.localtime()[2])
        self.labelMessage = QLabel(str(self.absent), self)
        self.labelMessage.move(100, 90)
        self.labelMessage.resize(50, 20)
        self.labelMessage.setStyleSheet("color:red")
        self.save_button = QPushButton('Save',self)
        self.save_button.move(50,130)
        self.save_button.resize(50,20)
        self.show()
        self.create_dir()


    def get_summary(self):
        self.absent = 0
        self.late = 0
        self.onTime = 0

        for student in self.studentList:
            if student.getAttendance()=="Absent":
                self.absent=self.absent+1
            elif student.getAttendance()=="Late":
                self.late=self.late+1
            else:
                self.onTime=self.onTime+1

    def create_dir(self):
        file_path_prefix = self.file_path[0:self.file_path.rfind("/")]
        if not os.path.exists(file_path_prefix+"/Attendance"):
            os.makedirs(file_path_prefix+"/Attendance")

    @pyqtSlot()
    def save_roster(self):
        self.students=[]
        for row in range(self.tableWidget.rowCount()):
            self.students.append(Student.Student(self.tableWidget.item(row, 3).text(),self.tableWidget.item(row, 1).text(),self.tableWidget.item(row, 2).text(),self.tableWidget.item(row, 0).text()))

        if self.file_extension=="csv":
            Export_File.exportCSV.exportToFile(object,self.file_name,self.students)
        elif self.file_extension=="xml":
            Export_File.exportXML.exportToFile(object,self.file_name,self.students)
        else:
            Export_File.exportJSON.exportToFile(object,self.file_name,self.students)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Attendance_For_The_Day()
    sys.exit(app.exec_())