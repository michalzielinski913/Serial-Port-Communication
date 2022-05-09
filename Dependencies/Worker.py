from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time
class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(str)

    def set_serial_and_window(self, serial, window):
        self.serial=serial
        self.window=window

    def run(self):
        """Long-running task."""
        while True:
            result=self.serial.readline()

            self.progress.emit(result.decode("utf-8") )
        self.finished.emit()