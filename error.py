# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class UiError(object):
    def setup_ui(self, error):
        error.setObjectName("error")
        error.resize(200, 130)
        error.setMinimumSize(QtCore.QSize(200, 130))
        error.setMaximumSize(QtCore.QSize(200, 130))
        self.centralwidget = QtWidgets.QWidget(error)
        self.centralwidget.setObjectName("centralwidget")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(20, 10, 160, 55))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("background-color: #a81111;\n"
                                       "color: white;\n"
                                       "border-radius: 20;")
        self.label_error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.label_message = QtWidgets.QLabel(self.centralwidget)
        self.label_message.setGeometry(QtCore.QRect(10, 75, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_message.setFont(font)
        self.label_message.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_message.setObjectName("label_message")
        error.setCentralWidget(self.centralwidget)

        self.retranslate_ui(error)
        QtCore.QMetaObject.connectSlotsByName(error)

    def retranslate_ui(self, error):
        _translate = QtCore.QCoreApplication.translate
        error.setWindowTitle(_translate("error", "MainWindow"))
        self.label_error.setText(_translate("error", "Error"))
        self.label_message.setText(_translate("error", "Files integrity\n"
                                                       "is broken"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    error = QtWidgets.QMainWindow()
    ui = UiError()
    ui.setup_ui(error)
    error.show()
    sys.exit(app.exec())