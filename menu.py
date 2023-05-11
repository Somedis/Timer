import sys

from PyQt6 import QtWidgets

from menu_ui import UiMenu


class MainMenu(QtWidgets.QMainWindow, UiMenu):
    """
    Class that describes the behavior of the main menu.
    """

    def __init__(self, parent=None) -> None:
        super(MainMenu, self).__init__(parent)
        self.setup_ui(self)

    def setup_ui(self, main_window):
        UiMenu.setup_ui(self, main_window)

        self.button_timer.clicked.connect(self.close)
        self.button_alarmClock.clicked.connect(self.close)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainMenu()
    ui.show()
    sys.exit(app.exec())
