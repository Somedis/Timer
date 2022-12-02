import sys
from datetime import timedelta

from PyQt6 import QtWidgets
from PyQt6.QtCore import QTime, QTimer

from timer_instal_ui import UiTimer


class Timer(UiTimer):

    def __init__(self) -> None:
        super(Timer, self).__init__()

    def setup_ui(self, timer_instal):
        UiTimer.setup_ui(self, timer_instal)

        self.transition = QtWidgets.QPushButton()

        self.current_time = QTimer()
        self.current_time.timeout.connect(self.show_time)
        self.current_time.start(1)

        self.button_back.clicked.connect(self.current_time.stop)

        self.label_time_left.setHidden(True)
        self.button_stop.setHidden(True)
        self.label_countdown.setHidden(True)
        self.button_continue.setHidden(True)
        self.button_reset.setHidden(True)

    def show_time(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.label_timeNum.setText(label_time)


class TimerFunc(QtWidgets.QMainWindow, Timer):

    def __init__(self) -> None:
        super(TimerFunc, self).__init__()
        self.setup_ui(self)

    def setup_ui(self, timer_instal):
        Timer.setup_ui(self, timer_instal)

        self.countdown = QTimer()
        self.countdown.setInterval(1)
        self.countdown.timeout.connect(self.display_time)

        self.button_run.clicked.connect(self.func_start)
        self.button_back.clicked.connect(self.countdown.stop)
        self.button_stop.clicked.connect(self.func_stop)
        self.button_reset.clicked.connect(self.func_reset)
        self.button_continue.clicked.connect(self.func_continue)

    def func_start(self):
        self.label_time_left.setHidden(False)
        self.button_stop.setHidden(False)
        self.label_countdown.setHidden(False)
        self.button_back.setHidden(True)

        self.spinbox_hour.setReadOnly(True)
        self.spinbox_min.setReadOnly(True)
        self.spinbox_sec.setReadOnly(True)

        self.button_run.setText('Timer started')
        self.button_run.setStyleSheet("QPushButton {    \n"
                                      "    color: #282e5c;\n"
                                      "    background-color: #3bf3d4\n"
                                      "}")
        self.countdown.start()

        hour = self.spinbox_hour.value()
        minute = self.spinbox_min.value()
        second = self.spinbox_sec.value()

        self.delta = timedelta(hours=hour, minutes=minute, seconds=second)

    def func_stop(self):
        self.countdown.stop()
        self.button_run.setText('Timer stopped')
        self.button_run.setStyleSheet("background-color: #a81111")

        self.button_stop.setHidden(True)
        self.button_continue.setHidden(False)
        self.button_reset.setHidden(False)
        self.button_back.setHidden(False)

    def func_reset(self):
        self.button_continue.setHidden(True)
        self.button_reset.setHidden(True)

        self.label_time_left.setHidden(True)
        self.label_countdown.setHidden(True)
        self.button_back.setHidden(False)

        self.spinbox_hour.setReadOnly(False)
        self.spinbox_min.setReadOnly(False)
        self.spinbox_sec.setReadOnly(False)

        self.button_run.setEnabled(True)
        self.button_run.setText('Run Timer')
        self.button_run.setStyleSheet("QPushButton {    \n"
                                      "    border: 3px solid #3051a8;\n"
                                      "    border-radius: 20;\n"
                                      "    color: white;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #3051a8\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: #3bf3d4\n"
                                      "}")

    def func_continue(self):
        self.button_back.setHidden(True)
        self.button_continue.setHidden(True)
        self.button_reset.setHidden(True)
        self.button_stop.setHidden(False)

        self.button_run.setText('Timer started')
        self.button_run.setStyleSheet("QPushButton {    \n"
                                      "    color: #282e5c;\n"
                                      "    background-color: #3bf3d4\n"
                                      "}")
        self.countdown.start()

    def display_time(self):
        mm, ss = divmod(self.delta.seconds + 1, 60)
        hh, mm = divmod(mm, 60)

        self.label_countdown.setText(f'{hh:02}:{mm:02}:{ss:02}')

        self.delta = self.delta - timedelta(seconds=0.001)

        if self.delta.days < 0:
            self.current_time.stop()
            self.countdown.stop()
            self.transition.click()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = TimerFunc()
    ui.show()
    sys.exit(app.exec())
