import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QPushButton, QComboBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize
from User_Interface import Display_Roster,Student_Login


class MainMenu(QWidget):

    def __init__(self, file_name,parent=None):
        super().__init__()
        self.title = 'Main Menu'
        self.left = 200
        self.top = 200
        self.width = 525
        self.height = 300
        self.file_name = file_name
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        window_font = QFont("Times", 20)
        window_font.setUnderline(True)
        colon_font = QFont("Times", 32)

        window_label = QLabel("Set Time Restrictions:", self)
        window_label.setFont(window_font)
        window_label.move(20, 20)

        start_label = QLabel("Start:", self)
        start_label.move(35, 80)

        self.time_box(35, 97.5, 115, 190, 100, True,"StartTime")

        dash_label = QLabel("-", self)
        dash_label.setFont(colon_font)
        dash_label.move(255, 100)

        end_label = QLabel("End:", self)
        end_label.move(275, 80)

        self.time_box(275, 337.5, 355, 430, 100, False,"EndTime")

        display_roster = QPushButton("Show Roster", self)
        display_roster.move(35, 230)
        display_roster.clicked.connect(self.show_table)

        change_file = QPushButton("", self)
        change_file.setToolTip("Change roster file")
        change_file.setIcon(QIcon('openfile.png'))
        change_file.setIconSize(QSize(20, 20))
        change_file.setMaximumSize(25, 22.5)
        change_file.move(432.5, 230)
        change_file.clicked.connect(self.change_file)

        button_submit = QPushButton("", self)
        button_submit.setIcon(QIcon('go.png'))
        button_submit.setIconSize(QSize(15, 15))
        button_submit.setMaximumSize(25, 22.5)
        button_submit.move(460, 230)
        button_submit.clicked.connect(self.submit_time)
    def time_box(self, hbx, clx, mbx, apx, y, start,position):
        colon_font = QFont("Times", 32)
        time_font = QFont("Times", 18)

        colon_label = QLabel(":", self)
        colon_label.setFont(colon_font)
        colon_label.move(clx, y)

        if position=="StartTime":
            self.left_hours_box = QComboBox(self)
            self.left_hours_box.setFixedSize(60, 60)
            self.left_hours_box.setFont(time_font)
            self.set_time(self.left_hours_box, 13)
            #hours_box.setCurrentIndex()
            self.left_hours_box.move(hbx, y)

            self.left_minutes_box = QComboBox(self)
            self.left_minutes_box.setFixedSize(60, 60)
            self.left_minutes_box.setFont(time_font)
            self.set_time(self.left_minutes_box, 60)
            self.left_minutes_box.move(mbx, y)

            self.left_am_pm_box = QComboBox(self)
            self.left_am_pm_box.setFixedSize(60, 60)
            self.left_am_pm_box.setFont(time_font)
            self.left_am_pm_box.addItem("AM")
            self.left_am_pm_box.addItem("PM")
            self.left_am_pm_box.move(apx, y)

            hours = time.localtime()[3]
            minutes = time.localtime()[4]
            am_pm = None

            if hours < 12:
                am_pm = 0
            elif hours == 12:
                am_pm = 1
            else:
                hours = hours - 12
                am_pm = 1

            if start:
                self.left_hours_box.setCurrentIndex(hours - 1)
                self.left_minutes_box.setCurrentIndex(minutes - 1)
                self.left_am_pm_box.setCurrentIndex(am_pm)

        else:
            self.right_hours_box = QComboBox(self)
            self.right_hours_box.setFixedSize(60, 60)
            self.right_hours_box.setFont(time_font)
            self.set_time(self.right_hours_box, 13)
            # hours_box.setCurrentIndex()
            self.right_hours_box.move(hbx, y)

            self.right_minutes_box = QComboBox(self)
            self.right_minutes_box.setFixedSize(60, 60)
            self.right_minutes_box.setFont(time_font)
            self.set_time(self.right_minutes_box, 60)
            self.right_minutes_box.move(mbx, y)

            self.right_am_pm_box = QComboBox(self)
            self.right_am_pm_box.setFixedSize(60, 60)
            self.right_am_pm_box.setFont(time_font)
            self.right_am_pm_box.addItem("AM")
            self.right_am_pm_box.addItem("PM")
            self.right_am_pm_box.move(apx, y)

            hours = time.localtime()[3]
            minutes = time.localtime()[4]
            am_pm = None

            if hours < 12:
                am_pm = 0
            elif hours == 12:
                am_pm = 1
            else:
                hours = hours - 12
                am_pm = 1

            if start:
                self.right_hours_box.setCurrentIndex(hours - 1)
                self.right_minutes_box.setCurrentIndex(minutes - 1)
                self.right_am_pm_box.setCurrentIndex(am_pm)

    def set_time(self, combobox, stop):
        for i in range(1, stop):
            combobox.addItem(str(i))

    def show_table(self):
        self.display_table = Display_Roster.App(self.file_name)
        self.display_table.show()

    def change_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            self.file_name = files[0]
    def submit_time(self):
        startHour=int(self.left_hours_box.currentText())
        startMin = int(self.left_minutes_box.currentText())
        endHour = int(self.right_hours_box.currentText())
        endMin = int(self.right_minutes_box.currentText())

        timeFrame=(endHour-startHour)*3600+(endMin-startMin)*60
        self.menu = Student_Login.StudentLogin(timeFrame)
        self.menu.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = MainMenu()
    admin.show()
    sys.exit(app.exec_())