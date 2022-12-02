import sys
from datetime import timedelta

from PyQt6 import QtWidgets
from PyQt6.QtCore import QDate, QDateTime, QTime, QTimer

from alarm_clock_instal_ui import UiAlarmClock


class AlarmClock(UiAlarmClock):

    def __init__(self) -> None:
        super(AlarmClock, self).__init__()
        self.setup_ui(self)

    def setup_ui(self, ac_instal):
        UiAlarmClock.setup_ui(self, ac_instal)

        self.time = QTimer()
        self.time.timeout.connect(self.show_time)
        self.time.start(1)

        self.date = QTimer()
        self.date.timeout.connect(self.show_date)
        self.date.start(1)

        self.setdatetime = QTimer()
        self.setdatetime.timeout.connect(self.set_datetime)
        self.setdatetime.start(1)

        self.button_back.clicked.connect(self.time.stop)
        self.button_back.clicked.connect(self.date.stop)
        self.button_back.clicked.connect(self.setdatetime.stop)

        self.button_stop.setHidden(True)
        self.button_reset.setHidden(True)
        self.label_countdown.setHidden(True)

        self.button_run.clicked.connect(self.hiding_ui)
        self.button_run.clicked.connect(self.adding_ui)

        date_format = 'dd.MM.yyyy hh:mm:ss'
        self.dateTimeEdit.setDisplayFormat(date_format)

    def set_datetime(self):
        self.dateTimeEdit.setMinimumDate(QDate.currentDate())
        self.dateTimeEdit.setMinimumTime(QTime.currentTime())

    def show_time(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.label_numTime.setText(label_time)

    def show_date(self):
        current_date = QDate.currentDate()
        label_date = current_date.toString('dd.MM.yyyy')
        self.label_numDate.setText(label_date)

    def hiding_ui(self):
        self.button_back.setHidden(True)
        self.button_run.setHidden(True)
        self.dateTimeEdit.setHidden(True)

    def adding_ui(self):
        self.button_stop.setHidden(False)
        self.label_countdown.setHidden(False)
        self.label_setdat.setText('Alarm Clock started')
        self.label_setdat.setStyleSheet("border-radius: 20;\n"
                                        "color: #282e5c;\n"
                                        "background-color: #3bf3d4")


class AlarmClockFunc(QtWidgets.QMainWindow, AlarmClock):

    def __init__(self) -> None:
        super(AlarmClockFunc, self).__init__()
        self.setup_ui(self)

    def setup_ui(self, ac_instal):
        AlarmClock.setup_ui(self, ac_instal)

        self.transition = QtWidgets.QPushButton()

        self.countdown = QTimer()
        self.countdown.setInterval(1)
        self.countdown.timeout.connect(self.display_time)

        self.button_run.clicked.connect(self.func_start)
        self.button_stop.clicked.connect(self.func_stop)
        self.button_reset.clicked.connect(self.func_reset)

    def func_start(self):
        self.countdown.start()

        current_datetime = QDateTime.currentDateTime()
        self.start_date_py = current_datetime.toPyDateTime()
        end_date = self.dateTimeEdit.dateTime()
        self.end_date_py = end_date.toPyDateTime()

        self.delta = self.end_date_py - self.start_date_py

    def func_stop(self):
        self.countdown.stop()
        self.button_stop.setHidden(True)
        self.button_reset.setHidden(False)
        self.button_back.setHidden(False)
        self.label_setdat.setText('Alarm Clock stopped')
        self.label_setdat.setStyleSheet("background-color: #a81111;\n"
                                        "color: #282e5c")

    def func_reset(self):
        self.button_reset.setHidden(True)
        self.label_countdown.setHidden(True)

        self.button_run.setHidden(False)
        self.dateTimeEdit.setHidden(False)
        self.button_back.setHidden(False)
        self.label_setdat.setText('Set date and time')
        self.label_setdat.setStyleSheet("color: #ff5398")

    def display_time(self):
        mm, ss = divmod(self.delta.seconds + 1, 60)
        hh, mm = divmod(mm, 60)

        self.label_countdown.setText(
            f'{self.delta.days} дн. {hh:02} час. {mm:02} мин. {ss:02} сек.')

        self.delta = self.delta - timedelta(seconds=0.001)

        if self.delta.days < 0:
            self.countdown.stop()
            self.time.stop()
            self.date.stop()
            self.setdatetime.stop()
            self.transition.click()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = AlarmClockFunc()
    ui.show()
    sys.exit(app.exec())
