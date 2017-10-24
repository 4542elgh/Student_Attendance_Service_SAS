import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from User_Interface import Display_Roster


class LoadRoster(QWidget):
    file_pass = ""

    def __init__(self, parent=None):
        super().__init__()
        self.title = 'Load Roster'
        self.left = 200
        self.top = 200
        self.width = 600
        self.height = 400
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label_filename = QLabel('Path:', self)
        label_filename.move(65, 305)

        textbox_filename = QLineEdit(self)
        textbox_filename.setObjectName("line")
        textbox_filename.resize(400, 20)
        textbox_filename.move(100, 300)

        button_file = QPushButton('', self)
        button_file.setIcon(QIcon('openfile.png'))
        button_file.setIconSize(QSize(20, 20))
        button_file.setMaximumSize(25, 22.5)
        button_file.move(505, 299)
        button_file.clicked.connect(self.open_file_names_dialog)

        button_submit = QPushButton('', self)
        button_submit.setIcon(QIcon('go.png'))
        button_submit.setIconSize(QSize(15, 15))
        button_submit.setMaximumSize(25, 22.5)
        button_submit.move(535, 299)
        button_submit.clicked.connect(self.open_set_parameter)

    def open_file_names_dialog(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            file_name = files[0]
            self.file_pass = file_name
            line = self.findChild(QLineEdit, "line")
            line.setText(file_name)

    def open_set_parameter(self):
        self.close()
        self.set_parameter = Display_Roster.App(self.file_pass)
        self.set_parameter.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    load_roaster = LoadRoster()
    load_roaster.show()
    sys.exit(app.exec_())