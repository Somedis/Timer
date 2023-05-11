import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer

from alarm_clock_result_ui import UiAlarmClockResult


class AlarmClockResultFunc(QtWidgets.QMainWindow, UiAlarmClockResult):
    """
    Class that adds the ability to play an audio track for an alarm clock.
    """

    def __init__(self) -> None:
        super(AlarmClockResultFunc, self).__init__()

    def setup_ui(self, ac_result):
        UiAlarmClockResult.setup_ui(self, ac_result)

        filename = "sounds/Alarm Clock.mp3"
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(filename))
        self.audio_output.setVolume(50)
        self.player.setLoops(100)
        self.player.play()

        self.button_menu.clicked.connect(self.player.stop)
        self.button_restart.clicked.connect(self.player.stop)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ac_result = QtWidgets.QMainWindow()
    ui = AlarmClockResultFunc()
    ui.setup_ui(ac_result)
    ac_result.show()
    sys.exit(app.exec())
