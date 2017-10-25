import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

from Import_Export import Export_File
from Import_Export import Import_File
from Add_Edit_Delete import ModifyEntry
from User_Interface import Display_Roster


class App(QWidget):
    def __init__(self, file_name):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.left = 200
        self.top = 200
        self.width = 600
        self.height = 400
        self.file_name = file_name
        self.file_extension = self.file_name[self.file_name.rfind(".") + 1:]
        self.students = self.parse_file()

        self.initUI()


    def initUI(self):
        self.setWindowTitle("Displaying Roster for") #have a method to get the file name for class indication
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def parse_file(self):
        if self.file_extension == "csv":
            return Import_File.importCSV().toList(self.file_name)

        elif self.file_extension == "xml":
            return Import_File.importXML.toList(object, self.file_name)

        elif self.file_extension == "json":
            return Import_File.importJSON.toList(object, self.file_name)

    def createTable(self):
        # Create table

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.students)) #get the total # of student list length
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setFixedHeight(325)
        self.tableWidget.move(100,100)

        self.tableWidget.setHorizontalHeaderLabels("CIN;First Name;Last Name;Serial Number;Operation".split(";"))
        
        counter=0
        for student in self.students:
            student.getFirstName()

            self.tableWidget.setItem(counter,0,QTableWidgetItem(student.getCIN()))
            self.tableWidget.setItem(counter,1, QTableWidgetItem(student.getFirstName()))
            self.tableWidget.setItem(counter,2, QTableWidgetItem(student.getLastName()))
            self.tableWidget.setItem(counter,3, QTableWidgetItem(student.getSerial()))
            self.btn_sell = QPushButton('Edit')
            self.tableWidget.setCellWidget(counter, 4,self.btn_sell)
            counter=counter+1
        # self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        # self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        # self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        # self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        # self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        # self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        # self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        # self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        # self.tableWidget.move(0, 0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())