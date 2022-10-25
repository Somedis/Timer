import sys

from PyQt6 import QtWidgets

from menu import MainMenu

from timer import TimerUpdate3

from timer_end_ui import UiTimerEnd


class StartMenu:

    def __init__(self) -> None:
        super(StartMenu, self).__init__()
        self.firstWindow = MainMenu()
        self.secondWindow = TimerUpdate3()
        self.thirdWindow = UiTimerEnd()
        # self.main_menu()

    def main_menu(self):
        self.firstWindow.setupUi(self)
        self.firstWindow.timer_btn.clicked.connect(self.second_win)

    def second_win(self):
        self.secondWindow.setupUi(self)
        self.secondWindow.back_btn.clicked.connect(self.main_menu)
        # self.secondWindow.set.
        # self.secondWindow.run_btn.clicked.connect(self.secondWindow.run_timer)

    def third_win(self):
        self.thirdWindow.setupUi(self)
        self.thirdWindow.menu_btn.clicked.connect(self.main_menu)
        self.thirdWindow.res_btn.clicked.connect(self.second_win)


class Timer(QtWidgets.QMainWindow, StartMenu):

    def __init__(self) -> None:
        super(Timer, self).__init__()
        self.main_menu()

    # def set_timer(self):
    #     Timer_Win2_Upd1.set_timer(self)
    #     self.fourth_win()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ui = Timer()
    ui.show()
    sys.exit(app.exec())
