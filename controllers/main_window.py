from PySide6.QtWidgets import QWidget, QMainWindow

from views.main_window_ui import Ui_MainWindow

class MainWindowForm(QMainWindow, QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.test_button.clicked.connect(self.hello)

    def hello(self):
        print('Hello World')