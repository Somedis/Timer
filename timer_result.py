import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer

from timer_result_ui import UiTimerResult


class TimerResultFunc(QtWidgets.QMainWindow, UiTimerResult):
    """
    Class that adds the ability to play an audio track for a timer.
    """

    def __init__(self) -> None:
        super(TimerResultFunc, self).__init__()

    def setup_ui(self, timer_result):
        UiTimerResult.setup_ui(self, timer_result)

        filename = "sounds/Timer.mp3"
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(filename))
        self.audio_output.setVolume(50)
        self.player.setLoops(100)
        self.player.play()

        self.button_menu.clicked.connect(self.player.stop)
        self.button_restart.clicked.connect(self.player.stop)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    timer_result = QtWidgets.QMainWindow()
    ui = TimerResultFunc()
    ui.setup_ui(timer_result)
    timer_result.show()
    sys.exit(app.exec())
