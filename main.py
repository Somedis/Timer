import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from Alarmclock_Timer import Ui_MainWindow



class StartMenu(QtWidgets.QMainWindow):

    def __init__(self) -> None:
        super(StartMenu, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = StartMenu()
    application.show()

    sys.exit(app.exec())
    pass