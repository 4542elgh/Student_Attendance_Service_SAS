import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QPushButton, QComboBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize
from User_Interface import Display_Roster


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

        self.time_box(35, 97.5, 115, 190, 100, True)

        dash_label = QLabel("-", self)
        dash_label.setFont(colon_font)
        dash_label.move(255, 100)

        end_label = QLabel("End:", self)
        end_label.move(275, 80)

        self.time_box(275, 337.5, 355, 430, 100, False)

        display_roster = QPushButton("Show Roster", self)
        display_roster.move(35, 230)

        change_file = QPushButton("", self)
        change_file.setToolTip("Change roster file")
        change_file.setIcon(QIcon('openfile.png'))
        change_file.setIconSize(QSize(20, 20))
        change_file.setMaximumSize(25, 22.5)
        change_file.move(432.5, 230)

        button_submit = QPushButton("", self)
        button_submit.setIcon(QIcon('go.png'))
        button_submit.setIconSize(QSize(15, 15))
        button_submit.setMaximumSize(25, 22.5)
        button_submit.move(460, 230)

    def time_box(self, hbx, clx, mbx, apx, y, start):
        colon_font = QFont("Times", 32)
        time_font = QFont("Times", 18)

        hours_box = QComboBox(self)
        hours_box.setFixedSize(60, 60)
        hours_box.setFont(time_font)
        self.set_time(hours_box, 13)
        #hours_box.setCurrentIndex()
        hours_box.move(hbx, y)

        colon_label = QLabel(":", self)
        colon_label.setFont(colon_font)
        colon_label.move(clx, y)

        minutes_box = QComboBox(self)
        minutes_box.setFixedSize(60, 60)
        minutes_box.setFont(time_font)
        self.set_time(minutes_box, 60)
        minutes_box.move(mbx, y)

        am_pm_box = QComboBox(self)
        am_pm_box.setFixedSize(60, 60)
        am_pm_box.setFont(time_font)
        am_pm_box.addItem("AM")
        am_pm_box.addItem("PM")
        am_pm_box.move(apx, y)

        hours = time.localtime()[3]
        minutes = time.localtime()[4]
        am_pm = None

        if hours < 12:
            am_pm = 0
        else:
            hours = hours - 12
            am_pm = 1

        if start:
            hours_box.setCurrentIndex(hours - 1)
            minutes_box.setCurrentIndex(minutes - 1)
            am_pm_box.setCurrentIndex(am_pm)

    def set_time(self, combobox, stop):
        for i in range(1, stop):
            combobox.addItem(str(i))

    def show_table(self):
        print()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = MainMenu()
    admin.show()
    sys.exit(app.exec_())