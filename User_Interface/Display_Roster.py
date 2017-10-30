import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton,QHBoxLayout,QMessageBox
from PyQt5.QtCore import pyqtSlot,QEvent
from PyQt5 import QtCore
from Import_Export import Import_File,Export_File
from Add_Edit_Delete import ModifyEntry
from Student import Student

class App(QWidget):
    def __init__(self, file_name):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.left = 200
        self.top = 200
        self.width = 665
        self.height = 400
        self.file_name = file_name
        self.file_prefix=self.file_name[self.file_name.rfind("/")+1:self.file_name.rfind(".")]
        self.file_extension = self.file_name[self.file_name.rfind(".") + 1:]
        self.students = self.parse_file()
        self.modifyEntry = ModifyEntry.Modify_Entry
        self.file_type=None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Displaying Roster for "+str(self.file_prefix))  # have a method to get the file name for class indication
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)

        hbox = QHBoxLayout()
        hbox.addStretch(1)

        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.save_roster)
        self.discard_button = QPushButton('Discard')
        self.discard_button.clicked.connect(self.discard_roster_change)

        hbox.addWidget(self.save_button)
        hbox.addWidget(self.discard_button)
        self.layout.addStretch(1)

        self.layout.addLayout(hbox)

        self.setLayout(self.layout)
        # self.tableWidget.doubleClicked(self.on_click)
        self.show()

    def parse_file(self):
        if self.file_extension == "csv":
            self.file_type="csv"
            return Import_File.importCSV().toList(self.file_name)

        elif self.file_extension == "xml":
            self.file_type = "xml"
            return Import_File.importXML.toList(object, self.file_name)

        elif self.file_extension == "json":
            self.file_type = "json"
            return Import_File.importJSON.toList(object, self.file_name)

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.students))  # get the total # of student list length
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setFixedHeight(325)
        self.tableWidget.setHorizontalHeaderLabels("CIN;First Name;Last Name;Serial Number;Delete".split(";"))
        App.generate_Table(self)

        # self.layout.addWidget(self.discard_button)
        # self.delete_button.clicked.connect(lambda state, x=student.getCIN(), y=counter: self.on_click_delete(x, y))

    def generate_Table(self):
        counter = 0
        for student in self.students:
            self.tableWidget.setItem(counter, 0, QTableWidgetItem(student.getCIN()))
            self.tableWidget.setItem(counter, 1, QTableWidgetItem(student.getFirstName()))
            self.tableWidget.setItem(counter, 2, QTableWidgetItem(student.getLastName()))
            self.tableWidget.setItem(counter, 3, QTableWidgetItem(student.getSerial()))
            self.delete_button = QPushButton('Delete')
            self.delete_button.clicked.connect(lambda state, x=student.getCIN(), y=counter: self.on_click_delete(x, y))
            self.tableWidget.setCellWidget(counter, 4, self.delete_button)
            counter = counter + 1

    @pyqtSlot()
    def save_roster(self):
        self.students=[]
        for row in range(self.tableWidget.rowCount()):
            self.students.append(Student.Student(self.tableWidget.item(row, 3).text(),self.tableWidget.item(row, 1).text(),self.tableWidget.item(row, 2).text(),self.tableWidget.item(row, 0).text()))
        if self.file_type=="csv":
            Export_File.exportCSV.exportToFile(self.students)
        elif self.file_type=="xml":
            Export_File.exportXML.exportToFile(self.students)
        else:
            Export_File.exportJSON.exportToFile(self.students)

    def discard_roster_change(self):
        QMessageBox.question(self, 'Student Attendance Service', "Changes has been discarded",QMessageBox.Ok)
        self.close()

    def on_click_delete(self,cin,rowNum):
        for student in self.students:
            if student.getCIN() == cin:
                self.tableWidget.removeRow(rowNum)
                self.students.remove(student)
                print(cin)
                print(rowNum)
        App.generate_Table(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())