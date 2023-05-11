import os
import sys

from PyQt6 import QtWidgets

from alarm_clock_instal import AlarmClockFunc

from alarm_clock_result import AlarmClockResultFunc

from error import UiError

from menu import MainMenu

from timer_instal import TimerFunc

from timer_result import TimerResultFunc


class CheckFiles():
    """
    Class of file integrity checker.
    """

    FOLDERS = ('sounds', 'pics', 'fonts')
    SOUNDS = ('Alarm Clock.mp3', 'Timer.mp3')
    PICTURES = ('alarmclock_instal.png', 'alarmclock_menu.png', 'alarmclock_result.png',
                'send_time.png', 'timer_instal.png', 'timer_menu.png', 'timer_result.png')
    FONTS = ('unispace bd.ttf', )

    def check_folders(self):
        """
        Folder check function.
        """
        self.current_dir = os.getcwd()
        self.files_list = os.listdir(self.current_dir)
        for folder in __class__.FOLDERS:
            if folder in self.files_list:
                pass
            else:
                return 0

    def check_sounds(self):
        """
        Sound check function.
        """
        if self.check_folders() != 0:
            for sound in __class__.SOUNDS:
                if sound in os.listdir('sounds'):
                    pass
                else:
                    return 0
        else:
            return 0

    def check_pics(self):
        """
        Pictures check function.
        """
        if self.check_folders() != 0:
            for pics in __class__.PICTURES:
                if pics in os.listdir('pics'):
                    pass
                else:
                    return 0
        else:
            return 0

    def check_fonts(self):
        """
        Fonts check function.
        """
        if self.check_folders() != 0:
            for font in __class__.FONTS:
                if font in os.listdir('fonts'):
                    pass
                else:
                    return 0
        else:
            return 0


class StartMenu(QtWidgets.QMainWindow, CheckFiles):
    """
    Control class that links individual GUIs to each other.
    """

    def __init__(self) -> None:
        super(StartMenu, self).__init__()

        self.error = UiError()

        self.menu = MainMenu()
        self.timer = TimerFunc()
        self.timerResult = TimerResultFunc()
        self.alarmClock = AlarmClockFunc()
        self.alarmClockResult = AlarmClockResultFunc()

        self.start_program()

    def start_program(self):
        """
        Function that checks the integrity of files and launches a program.
        """
        if self.check_sounds() != 0:
            if self.check_pics() != 0:
                if self.check_fonts() != 0:
                    self.main_menu()
                else:
                    self.error.setup_ui(self)
            else:
                self.error.setup_ui(self)
        else:
            self.error.setup_ui(self)

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
