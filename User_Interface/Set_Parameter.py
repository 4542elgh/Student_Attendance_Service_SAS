import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class SetParameter(QMainWindow):
    def __init__(self, file_name, parent=None):
        super().__init__()
        self.title = 'Set Parameters'
        self.left = 200
        self.top = 200
        self.width = 600
        self.height = 400
        self.file_name = file_name
        self.init_ui()

    def init_ui(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        file = QLabel(self)
        file.setText(self.file_name)
        file.move(300, 200)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     parameter = SetParameter()
#     parameter.show()
#     sys.exit(app.exec_())