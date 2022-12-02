# Form implementation generated from reading ui file 'timer_instal.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class UiTimer(object):
    def setup_ui(self, timer_instal):
        timer_instal.setObjectName("timer_instal")
        timer_instal.resize(600, 500)
        timer_instal.setMinimumSize(QtCore.QSize(600, 500))
        timer_instal.setMaximumSize(QtCore.QSize(600, 500))
        timer_instal.setAutoFillBackground(False)
        timer_instal.setStyleSheet("background-color: #0d1131;")
        self.centralwidget = QtWidgets.QWidget(timer_instal)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setGeometry(QtCore.QRect(10, 10, 580, 480))
        self.frame_main.setStyleSheet("background-color: #181b3f;\n"
                                      "border-radius: 20")
        self.frame_main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_main.setObjectName("frame_main")
        self.frame_up = QtWidgets.QFrame(self.frame_main)
        self.frame_up.setGeometry(QtCore.QRect(0, 0, 580, 130))
        self.frame_up.setStyleSheet("background-color: #282e5c;\n"
                                    "border-radius: 20")
        self.frame_up.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_up.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_up.setObjectName("frame_up")
        self.label_title = QtWidgets.QLabel(self.frame_up)
        self.label_title.setGeometry(QtCore.QRect(120, 45, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: white")
        self.label_title.setObjectName("label_title")
        self.label_pic = QtWidgets.QLabel(self.frame_up)
        self.label_pic.setGeometry(QtCore.QRect(20, 20, 101, 81))
        self.label_pic.setText("")
        self.label_pic.setPixmap(QtGui.QPixmap("pics/timer_instal.png"))
        self.label_pic.setObjectName("label_pic")
        self.button_back = QtWidgets.QPushButton(self.frame_up)
        self.button_back.setGeometry(QtCore.QRect(480, 45, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_back.setFont(font)
        self.button_back.setStyleSheet("QPushButton {    \n"
                                       "    border: 3px solid #a81111;\n"
                                       "    background-color: #700404;\n"
                                       "    border-radius: 20;\n"
                                       "    color: white;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: #a81111\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: #610202;\n"
                                       "    border: 3px solid #610202;\n"
                                       "}")
        self.button_back.setObjectName("button_back")
        self.label_timeNow = QtWidgets.QLabel(self.frame_up)
        self.label_timeNow.setGeometry(QtCore.QRect(280, 10, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_timeNow.setFont(font)
        self.label_timeNow.setStyleSheet("color: #ff5398")
        self.label_timeNow.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_timeNow.setObjectName("label_timeNow")
        self.label_timeNum = QtWidgets.QLabel(self.frame_up)
        self.label_timeNum.setGeometry(QtCore.QRect(270, 60, 175, 50))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_timeNum.setFont(font)
        self.label_timeNum.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_timeNum.setStyleSheet("color: #3870ec;\n"
                                         "background-color: #1a1f4a")
        self.label_timeNum.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_timeNum.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_timeNum.setObjectName("label_timeNum")
        self.frame_down = QtWidgets.QFrame(self.frame_main)
        self.frame_down.setGeometry(QtCore.QRect(10, 140, 560, 331))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frame_down.setFont(font)
        self.frame_down.setStyleSheet("background-color: #282e5c;\n"
                                      "border-radius: 20")
        self.frame_down.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_down.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_down.setObjectName("frame_down")
        self.label_instraction = QtWidgets.QLabel(self.frame_down)
        self.label_instraction.setGeometry(QtCore.QRect(30, 10, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_instraction.setFont(font)
        self.label_instraction.setStyleSheet("color: #ff5398")
        self.label_instraction.setObjectName("label_instraction")
        self.spinbox_sec = QtWidgets.QSpinBox(self.frame_down)
        self.spinbox_sec.setGeometry(QtCore.QRect(465, 65, 50, 120))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.spinbox_sec.setFont(font)
        self.spinbox_sec.setStatusTip("")
        self.spinbox_sec.setWhatsThis("")
        self.spinbox_sec.setAccessibleName("")
        self.spinbox_sec.setAccessibleDescription("")
        self.spinbox_sec.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.spinbox_sec.setStyleSheet("QSpinBox\n"
                                       "{\n"
                                       "    selection-background-color: #282e5c;\n"
                                       "    color: white;\n"
                                       "    padding-right: 5px;\n"
                                       "    padding-left: 5px;\n"
                                       "    padding-top: 25px;\n"
                                       "    padding-bottom: 25px;\n"
                                       "}\n"
                                       "\n"
                                       "QSpinBox::up-button\n"
                                       "{\n"
                                       "    width:45px;\n"
                                       "    height: 30px;\n"
                                       "    right: 3px;\n"
                                       "    top: 2px;\n"
                                       "}\n"
                                       "\n"
                                       "QSpinBox::down-button\n"
                                       "{\n"
                                       "    width:45px;\n"
                                       "    height: 30px;\n"
                                       "    right: 3px;\n"
                                       "    bottom: 2 px;\n"
                                       "}")
        self.spinbox_sec.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.spinbox_sec.setWrapping(False)
        self.spinbox_sec.setFrame(True)
        self.spinbox_sec.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinbox_sec.setReadOnly(False)
        self.spinbox_sec.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinbox_sec.setSpecialValueText("")
        self.spinbox_sec.setKeyboardTracking(True)
        self.spinbox_sec.setMaximum(59)
        self.spinbox_sec.setObjectName("spinbox_sec")
        self.button_run = QtWidgets.QPushButton(self.frame_down)
        self.button_run.setGeometry(QtCore.QRect(180, 210, 200, 45))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_run.setFont(font)
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
                                      "    background-color: #3bf3d4;\n"
                                      "}")
        self.button_run.setObjectName("button_run")
        self.label_hours = QtWidgets.QLabel(self.frame_down)
        self.label_hours.setGeometry(QtCore.QRect(45, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_hours.setFont(font)
        self.label_hours.setStyleSheet("color: #4f5991\n"
                                       "")
        self.label_hours.setObjectName("label_hours")
        self.label_mins = QtWidgets.QLabel(self.frame_down)
        self.label_mins.setGeometry(QtCore.QRect(215, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_mins.setFont(font)
        self.label_mins.setStyleSheet("color: #4f5991\n"
                                      "")
        self.label_mins.setObjectName("label_mins")
        self.label_secs = QtWidgets.QLabel(self.frame_down)
        self.label_secs.setGeometry(QtCore.QRect(385, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_secs.setFont(font)
        self.label_secs.setStyleSheet("color: #4f5991\n"
                                      "")
        self.label_secs.setObjectName("label_secs")
        self.spinbox_hour = QtWidgets.QSpinBox(self.frame_down)
        self.spinbox_hour.setGeometry(QtCore.QRect(125, 65, 50, 120))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.spinbox_hour.setFont(font)
        self.spinbox_hour.setToolTip("")
        self.spinbox_hour.setStatusTip("")
        self.spinbox_hour.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.spinbox_hour.setAutoFillBackground(False)
        self.spinbox_hour.setStyleSheet("QSpinBox\n"
                                        "{\n"
                                        "    selection-background-color: #282e5c;\n"
                                        "    color: white;\n"
                                        "    padding-right: 5px;\n"
                                        "    padding-left: 5px;\n"
                                        "    padding-top: 25px;\n"
                                        "    padding-bottom: 25px;\n"
                                        "}\n"
                                        "\n"
                                        "QSpinBox::up-button\n"
                                        "{\n"
                                        "    width:45px;\n"
                                        "    height: 30px;\n"
                                        "    right: 3px;\n"
                                        "    top: 2px;\n"
                                        "}\n"
                                        "\n"
                                        "QSpinBox::up-arrow \n"
                                        "{\n"
                                        "    \n"
                                        "}\n"
                                        "\n"
                                        "QSpinBox::down-button\n"
                                        "{\n"
                                        "    width:45px;\n"
                                        "    height: 30px;\n"
                                        "    right: 3px;\n"
                                        "    bottom: 2 px;\n"
                                        "}")
        self.spinbox_hour.setWrapping(False)
        self.spinbox_hour.setFrame(True)
        self.spinbox_hour.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinbox_hour.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinbox_hour.setSpecialValueText("")
        self.spinbox_hour.setKeyboardTracking(True)
        self.spinbox_hour.setMaximum(24)
        self.spinbox_hour.setObjectName("spinbox_hour")
        self.spinbox_min = QtWidgets.QSpinBox(self.frame_down)
        self.spinbox_min.setGeometry(QtCore.QRect(295, 65, 50, 120))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.spinbox_min.setFont(font)
        self.spinbox_min.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.spinbox_min.setStyleSheet("QSpinBox\n"
                                       "{\n"
                                       "    selection-background-color: #282e5c;\n"
                                       "    color: white;\n"
                                       "    padding-right: 5px;\n"
                                       "    padding-left: 5px;\n"
                                       "    padding-top: 25px;\n"
                                       "    padding-bottom: 25px;\n"
                                       "}\n"
                                       "\n"
                                       "QSpinBox::up-button\n"
                                       "{\n"
                                       "    width:45px;\n"
                                       "    height: 30px;\n"
                                       "    right: 3px;\n"
                                       "    top: 2px;\n"
                                       "}\n"
                                       "\n"
                                       "QSpinBox::down-button\n"
                                       "{\n"
                                       "    width:45px;\n"
                                       "    height: 30px;\n"
                                       "    right: 3px;\n"
                                       "    bottom: 2 px;\n"
                                       "}")
        self.spinbox_min.setWrapping(False)
        self.spinbox_min.setFrame(True)
        self.spinbox_min.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinbox_min.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinbox_min.setSpecialValueText("")
        self.spinbox_min.setKeyboardTracking(True)
        self.spinbox_min.setMaximum(59)
        self.spinbox_min.setObjectName("spinbox_min")
        self.button_stop = QtWidgets.QPushButton(self.frame_down)
        self.button_stop.setEnabled(True)
        self.button_stop.setGeometry(QtCore.QRect(400, 270, 100, 45))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_stop.setFont(font)
        self.button_stop.setStyleSheet("QPushButton {    \n"
                                       "    border: 3px solid #a81111;\n"
                                       "    background-color: #700404;\n"
                                       "    border-radius: 20;\n"
                                       "    color: white;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: #a81111\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: #610202;\n"
                                       "    border: 3px solid #610202;\n"
                                       "}")
        self.button_stop.setDefault(False)
        self.button_stop.setObjectName("button_stop")
        self.label_countdown = QtWidgets.QLabel(self.frame_down)
        self.label_countdown.setGeometry(QtCore.QRect(200, 270, 181, 50))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_countdown.setFont(font)
        self.label_countdown.setStyleSheet("color: white")
        self.label_countdown.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_countdown.setObjectName("label_countdown")
        self.label_time_left = QtWidgets.QLabel(self.frame_down)
        self.label_time_left.setEnabled(False)
        self.label_time_left.setGeometry(QtCore.QRect(30, 275, 171, 40))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_left.setFont(font)
        self.label_time_left.setStyleSheet("color: #ff5398")
        self.label_time_left.setObjectName("label_time_left")
        self.button_reset = QtWidgets.QPushButton(self.frame_down)
        self.button_reset.setGeometry(QtCore.QRect(390, 210, 160, 45))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_reset.setFont(font)
        self.button_reset.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_reset.setStyleSheet("QPushButton {    \n"
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
                                        "    background-color: #3bf3d4;\n"
                                        "}")
        self.button_reset.setObjectName("button_reset")
        self.button_continue = QtWidgets.QPushButton(self.frame_down)
        self.button_continue.setGeometry(QtCore.QRect(390, 270, 160, 45))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_continue.setFont(font)
        self.button_continue.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_continue.setStyleSheet("QPushButton {    \n"
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
                                           "    background-color: #3bf3d4;\n"
                                           "}")
        self.button_continue.setObjectName("button_continue")
        timer_instal.setCentralWidget(self.centralwidget)

        self.retranslate_ui(timer_instal)
        QtCore.QMetaObject.connectSlotsByName(timer_instal)

    def retranslate_ui(self, timer_instal):
        _translate = QtCore.QCoreApplication.translate
        timer_instal.setWindowTitle(_translate("timer_instal", "MainWindow"))
        self.label_title.setText(_translate("timer_instal", "Timer"))
        self.button_back.setText(_translate("timer_instal", "Back"))
        self.label_timeNow.setText(_translate("timer_instal", "Time now"))
        self.label_timeNum.setText(_translate("timer_instal", "23:59:59"))
        self.label_instraction.setText(_translate("timer_instal", "Set the time for timer"))
        self.button_run.setText(_translate("timer_instal", "Run Timer"))
        self.label_hours.setText(_translate("timer_instal", "Hours"))
        self.label_mins.setText(_translate("timer_instal", "Min-s"))
        self.label_secs.setText(_translate("timer_instal", "Sec-s"))
        self.button_stop.setText(_translate("timer_instal", "Stop"))
        self.label_countdown.setText(_translate("timer_instal", "23:59:59"))
        self.label_time_left.setText(_translate("timer_instal", "Time left"))
        self.button_reset.setText(_translate("timer_instal", "Reset"))
        self.button_continue.setText(_translate("timer_instal", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    timer_instal = QtWidgets.QMainWindow()
    ui = UiTimer()
    ui.setup_ui(timer_instal)
    timer_instal.show()
    sys.exit(app.exec())
