# Form implementation generated from reading ui file 'alarm_clock_instal.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class UiAlarmClock(object):
    def setup_ui(self, ac_instal):
        """
        GUI start function.
        """
        ac_instal.setObjectName("ac_instal")
        ac_instal.resize(600, 500)
        ac_instal.setMinimumSize(QtCore.QSize(600, 500))
        ac_instal.setMaximumSize(QtCore.QSize(600, 500))
        ac_instal.setAutoFillBackground(False)
        ac_instal.setStyleSheet("background-color: #0d1131;")
        self.centralwidget = QtWidgets.QWidget(ac_instal)
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
        self.label_title.setGeometry(QtCore.QRect(120, 45, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: white")
        self.label_title.setObjectName("label_title")
        self.label_pick1 = QtWidgets.QLabel(self.frame_up)
        self.label_pick1.setGeometry(QtCore.QRect(20, 20, 101, 81))
        self.label_pick1.setText("")
        self.label_pick1.setPixmap(QtGui.QPixmap("pics/alarmclock_instal.png"))
        self.label_pick1.setObjectName("label_pick1")
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
        self.label_curDate = QtWidgets.QLabel(self.frame_down)
        self.label_curDate.setGeometry(QtCore.QRect(30, 10, 220, 50))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_curDate.setFont(font)
        self.label_curDate.setStyleSheet("color: #ff5398")
        self.label_curDate.setObjectName("label_curDate")
        self.button_run = QtWidgets.QPushButton(self.frame_down)
        self.button_run.setGeometry(QtCore.QRect(157, 270, 245, 45))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_run.setFont(font)
        self.button_run.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
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
        self.label_numTime = QtWidgets.QLabel(self.frame_down)
        self.label_numTime.setGeometry(QtCore.QRect(310, 70, 175, 50))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_numTime.setFont(font)
        self.label_numTime.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_numTime.setStyleSheet("color: #3870ec;\n"
                                         "background-color: #1a1f4a")
        self.label_numTime.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_numTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_numTime.setObjectName("label_numTime")
        self.label_curTime = QtWidgets.QLabel(self.frame_down)
        self.label_curTime.setGeometry(QtCore.QRect(310, 10, 220, 50))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_curTime.setFont(font)
        self.label_curTime.setStyleSheet("color: #ff5398")
        self.label_curTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_curTime.setObjectName("label_curTime")
        self.label_numDate = QtWidgets.QLabel(self.frame_down)
        self.label_numDate.setGeometry(QtCore.QRect(30, 70, 210, 50))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_numDate.setFont(font)
        self.label_numDate.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_numDate.setStyleSheet("color: #3870ec;\n"
                                         "background-color: #1a1f4a")
        self.label_numDate.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_numDate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_numDate.setObjectName("label_numDate")
        self.label_setdat = QtWidgets.QLabel(self.frame_down)
        self.label_setdat.setEnabled(False)
        self.label_setdat.setGeometry(QtCore.QRect(90, 140, 380, 50))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_setdat.setFont(font)
        self.label_setdat.setStyleSheet("color: #ff5398")
        self.label_setdat.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_setdat.setObjectName("label_setdat")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame_down)
        self.dateTimeEdit.setGeometry(QtCore.QRect(75, 200, 410, 50))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setStyleSheet("QDateTimeEdit\n"
                                        "{\n"
                                        "    color: white;\n"
                                        "    selection-background-color: #282e5c;\n"
                                        "}")
        self.dateTimeEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_countdown = QtWidgets.QLabel(self.frame_down)
        self.label_countdown.setGeometry(QtCore.QRect(20, 205, 520, 50))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_countdown.setFont(font)
        self.label_countdown.setStyleSheet("color: white")
        self.label_countdown.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_countdown.setObjectName("label_countdown")
        self.button_stop = QtWidgets.QPushButton(self.frame_down)
        self.button_stop.setEnabled(True)
        self.button_stop.setGeometry(QtCore.QRect(230, 270, 100, 45))
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
        self.button_reset = QtWidgets.QPushButton(self.frame_down)
        self.button_reset.setGeometry(QtCore.QRect(200, 270, 160, 45))
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
        ac_instal.setCentralWidget(self.centralwidget)

        self.retranslate_ui(ac_instal)
        QtCore.QMetaObject.connectSlotsByName(ac_instal)

    def retranslate_ui(self, ac_instal):
        _translate = QtCore.QCoreApplication.translate
        ac_instal.setWindowTitle(_translate("ac_instal", "MainWindow"))
        self.label_title.setText(_translate("ac_instal", "Alarm Clock"))
        self.button_back.setText(_translate("ac_instal", "Back"))
        self.label_curDate.setText(_translate("ac_instal", "Current date"))
        self.button_run.setText(_translate("ac_instal", "Run Alarm Clock"))
        self.label_numTime.setText(_translate("ac_instal", "23:59:59"))
        self.label_curTime.setText(_translate("ac_instal", "Current time"))
        self.label_numDate.setText(_translate("ac_instal", "24.02.2022"))
        self.label_setdat.setText(_translate("ac_instal", "Set date and time"))
        self.label_countdown.setText(_translate("ac_instal", "366 дн. 23 час. 55 мин. 36 сек."))
        self.button_stop.setText(_translate("ac_instal", "Stop"))
        self.button_reset.setText(_translate("ac_instal", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ac_instal = QtWidgets.QMainWindow()
    ui = UiAlarmClock()
    ui.setup_ui(ac_instal)
    ac_instal.show()
    sys.exit(app.exec())
