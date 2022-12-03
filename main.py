import sys

from PyQt6 import QtWidgets

from alarm_clock_instal import AlarmClockFunc

from alarm_clock_result import AlarmClockResultFunc

from menu import MainMenu

from timer_instal import TimerFunc

from timer_result import TimerResultFunc


class StartMenu(QtWidgets.QMainWindow):
    """
    Control class that links individual GUIs to each other.
    """

    def __init__(self) -> None:
        super(StartMenu, self).__init__()

        self.menu = MainMenu()
        self.timer = TimerFunc()
        self.timerResult = TimerResultFunc()
        self.alarmClock = AlarmClockFunc()
        self.alarmClockResult = AlarmClockResultFunc()

        self.main_menu()

    def main_menu(self):
        """
        Function of calling the main menu
        and connection with other graphical interfaces.
        """
        self.menu.setup_ui(self)
        self.menu.button_timer.clicked.connect(self.set_timer)
        self.menu.button_alarmClock.clicked.connect(self.set_alarm_clock)

    def set_timer(self):
        """
        Timer setting call function
        and connection with other graphical interfaces.
        """
        self.timer.setup_ui(self)
        self.timer.button_back.clicked.connect(self.main_menu)
        self.timer.transition.clicked.connect(self.result_timer)

    def result_timer(self):
        """
        Function to call the end of the timer
        and connection with other graphical interfaces.
        """
        self.timerResult.setup_ui(self)
        self.timerResult.button_menu.clicked.connect(self.main_menu)
        self.timerResult.button_restart.clicked.connect(self.set_timer)

    def set_alarm_clock(self):
        """
        Alarm clock setting call function
        and connection with other graphical interfaces.
        """
        self.alarmClock.setup_ui(self)
        self.alarmClock.button_back.clicked.connect(self.main_menu)
        self.alarmClock.transition.clicked.connect(self.result_alarm_clock)

    def result_alarm_clock(self):
        """
        Function to call the end of the alarm clock
        and connection with other graphical interfaces.
        """
        self.alarmClockResult.setup_ui(self)
        self.alarmClockResult.button_menu.clicked.connect(self.main_menu)
        self.alarmClockResult.button_restart.clicked.connect(self.set_alarm_clock)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ui = StartMenu()
    ui.show()
    sys.exit(app.exec())
