import threading
import time

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTime, QTimer

from timer_ui import UiTimer


class TimerUpdate(UiTimer):

    def __init__(self) -> None:
        super(TimerUpdate, self).__init__()

    def setup_ui(self, timer):
        UiTimer.setupUi(self, timer)

        self.current_time = QTimer()
        self.current_time.timeout.connect(self.show_time)
        self.current_time.start(1)

        self.back_btn.clicked.connect(self.current_time.stop)

        self.time_left_lab.setHidden(True)
        self.stop_btn.setHidden(True)
        self.countdown_lab.setHidden(True)

    def show_time(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.time_label.setText(label_time)


class TimerUpdate2(TimerUpdate):

    def __init__(self) -> None:
        super(TimerUpdate2, self).__init__()
        # self.setupUi(self)

    def setup_ui(self, timer):
        TimerUpdate.setupUi(self, timer)

        self.run_btn.clicked.connect(self.adding_Ui)
        self.stop_btn.clicked.connect(self.hiding_Ui)

    def adding_ui(self):
        self.time_left_lab.setHidden(False)
        self.stop_btn.setHidden(False)
        self.countdown_lab.setHidden(False)
        self.back_btn.setHidden(True)

        self.hour_sb.setReadOnly(True)
        self.min_sb.setReadOnly(True)
        self.sec_sb.setReadOnly(True)

        self.run_btn.setEnabled(False)
        self.run_btn.setStyleSheet("QPushButton {    \n"
                                   "    border-radius: 20;\n"
                                   "    color: #282e5c;\n"
                                   "    background-color: #3bf3d4\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: #3051a8\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: #3bf3d4\n"
                                   "}")

    def hiding_ui(self):
        self.time_left_lab.setHidden(True)
        self.stop_btn.setHidden(True)
        self.countdown_lab.setHidden(True)
        self.back_btn.setHidden(False)

        self.hour_sb.setReadOnly(False)
        self.min_sb.setReadOnly(False)
        self.sec_sb.setReadOnly(False)

        self.run_btn.setEnabled(True)
        self.run_btn.setStyleSheet("QPushButton {    \n"
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


class TimerUpdate3(QtWidgets.QMainWindow, TimerUpdate2):

    def __init__(self) -> None:
        super(TimerUpdate3, self).__init__()
        self.setupUi(self)

    def setup_ui(self, timer):
        TimerUpdate2.setupUi(self, timer)

        self.run_btn.clicked.connect(self.run_timer)

    def set_timer(self):
        hours = self.hour_sb.value()
        mins = self.min_sb.value()
        secs = self.sec_sb.value()
        time.sleep(hours * 3600 + mins * 60 + secs)
        # self.timesup()

    def run_timer(self):
        thr = threading.Thread(target=self.set_timer)
        thr.start()

    def timesup(self):
        self.label_4.setHidden(True)
        self.label_5.setHidden(True)
        self.label_6.setHidden(True)
        self.label_7.setHidden(True)
        self.time_left_lab.setHidden(True)
        self.countdown_lab.setHidden(True)

        self.hour_sb.setHidden(True)
        self.min_sb.setHidden(True)
        self.sec_sb.setHidden(True)

        self.back_btn.setHidden(True)
        self.run_btn.setHidden(True)
        self.stop_btn.setHidden(True)

        self.timeup_lab = QtWidgets.QLabel(self.frame_down)
        self.timeup_lab.setGeometry(QtCore.QRect(250, 100, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.timeup_lab.setFont(font)
        self.timeup_lab.setStyleSheet("color: #ff5398")
        self.timeup_lab.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.timeup_lab.setObjectName("timeup_lab")
        self.res_btn = QtWidgets.QPushButton(self.frame_down)
        self.res_btn.setGeometry(QtCore.QRect(50, 250, 200, 45))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.res_btn.setFont(font)
        self.res_btn.setStyleSheet("QPushButton {    \n"
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
        self.res_btn.setObjectName("res_btn")
        self.menu_btn = QtWidgets.QPushButton(self.frame_down)
        self.menu_btn.setGeometry(QtCore.QRect(310, 250, 200, 45))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.menu_btn.setFont(font)
        self.menu_btn.setStyleSheet("QPushButton {    \n"
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
        self.menu_btn.setObjectName("menu_btn")
        self.pick_lab = QtWidgets.QLabel(self.frame_down)
        self.pick_lab.setGeometry(QtCore.QRect(40, 20, 191, 181))
        self.pick_lab.setText("")
        self.pick_lab.setPixmap(QtGui.QPixmap("../../Desktop/Python/timer/timer_icon2_1_4.png"))
        self.pick_lab.setObjectName("pick_lab")


class TimerThread(QtCore.QThread):

    any_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None) -> None:
        super(TimerThread, self).__init__(parent)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TimerUpdate3()
    ui.show()
    sys.exit(app.exec())
