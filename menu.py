from PyQt6 import QtWidgets

from menu_ui import UiMainWindow


class MainMenu(QtWidgets.QMainWindow, UiMainWindow):

    def __init__(self, parent=None) -> None:
        super(MainMenu, self).__init__(parent)
        self.setup_ui(self)

    def setup_ui(self, main_window):
        UiMainWindow.setup_ui(self, main_window)

        self.timer_btn.clicked.connect(self.close)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainMenu()
    ui.show()
    sys.exit(app.exec())
