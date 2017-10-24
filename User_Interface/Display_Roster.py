import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

from Import_Export import Export_File
from Import_Export import Import_File
from Add_Edit_Delete import ModifyEntry
from User_Interface import Display_Roster

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 200
        self.top = 200
        self.width = 600
        self.height = 400
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Dispaying Roster for") #have a method to get the file name for class indication
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        # Create table

        Export_File.exportCSV.exportToFile(object, [["1", "Evan", "Liu", "922"]])
        xml = Import_File.importCSV.toList(object)
        xml2 = ModifyEntry.Modify_Entry.Add_Entry(object, xml, "3", "Sherry", "Liu", "253")

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(xml2)) #get the total # of student list length
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(("CIN;First Name;Last Name;Serial Number").split(";"))
        
        counter=0
        for student in xml2:
            self.tableWidget.setItem(counter,0,QTableWidgetItem(student.getCIN()))
            self.tableWidget.setItem(counter,1, QTableWidgetItem(student.getFirstName()))
            self.tableWidget.setItem(counter,2, QTableWidgetItem(student.getLastName()))
            self.tableWidget.setItem(counter,3, QTableWidgetItem(student.getSerial()))
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